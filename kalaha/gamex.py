# class Player
# class Cup
# class Store
# class Move
# class Kalaha

from typing import Dict, List, Tuple, Optional, Union, Iterable
from enum import Enum

N_COLS = 6


class Player(Enum):
    BOTTOM = 0
    TOP = 1
    BLANK = -1

    def store(self):
        """
        Returns the store that marbles of the given player have to reach to score a point
        """
        if self == Player.BOTTOM:
            return N_COLS
        elif self == Player.TOP:
            return 0
        else:
            raise ValueError("Blank player has no goal coordinates")

    def opponent(self):
        """
        Returns the opponent Player object
        """
        if self == Player.BOTTOM:
            return Player.TOP
        elif self == Player.TOP:
            return Player.BOTTOM
        else:
            raise ValueError("Blank player has no opponents")

    def is_empty(self):
        return self == Player.BLANK

    def is_player(self):
        return self != Player.BLANK

    def get_repr(self):
        if self == Player.BOTTOM:
            return "B"
        elif self == Player.TOP:
            return "T"
        else:
            return "NA"


class Cup:
    def __init__(self, player: Player, col: int):
        self.side = player
        self.col = col
        self.marbles = 4

    def __init__(self, player: Player, col: int, marbles: int):
        self.side = player
        self.col = col
        self.marbles = marbles

    def next_cup(self):
        # if bottom player side and last cup
        if (self.col == N_COLS & self.side == Player.BOTTOM):
            return Store(Player.BOTTOM)
        # if top player side and last cup
        elif (self.col == 0 & self.side == Player.TOP):
            return Store(Player.TOP)
        # if any bottom player's cup
        elif (self.side == Player.BOTTOM):
            return Cup(self.side, self.col+1)
        # else any top player's cup
        else:
            return Cup(self.side, self.col-1)

    def get_marbles(self):
        return self.marbles

    def get_col(self):
        return self.col


class Store:
    def __init__(self, player: Player):
        self.player = player
        self.score = 0

    def __init__(self, player: Player, score):
        self.player = player
        self.score = score

    def get_score(self):
        return self.score

# two lists of cups for a player, with pointer to next cup
# each cup says who the player it belongs to and the number of marbles in cup


class Move:
    def __init__(self, player: Player, cup: Cup):
        self.player = player
        self.cup = cup
        self.next_cup = Cup.next_cup(cup)

    # def apply(self, game: Kalaha):
    #     game.move_marbles(self.cup)


class Kalaha(object):
    """
    The game state
    """

    def __init__(self):
        self.turn: Player = Player.BOTTOM
        self.sides = {
            Player.TOP: [Cup(Player.TOP, i, 4) for i in range(N_COLS)],
            Player.BOTTOM: [Cup(Player.BOTTOM, i, 4) for i in range(N_COLS)]
        }
        # self.sides = {
        #     Player.TOP: [Cup(Player.TOP, 0), Cup(Player.TOP, 1)],
        #     Player.BOTTOM: [Cup(Player.BOTTOM, i) for i in range(N_COLS)]
        # }
        self.stores = {
            Player.TOP: Store(Player.TOP, 0),
            Player.BOTTOM: Store(Player.BOTTOM, 0)
        }
        self.score = {Player.TOP: 0, Player.BOTTOM: 0}
        # self.actions = self.possible_actionas()
        self.winner = Player.BLANK

    def get_players_cups(self, player: Player) -> List[Cup]:
        return self.sides[player]

    def get_cup_by_id(self, player, number) -> Cup:
        return self.sides[player][number]

    def check_game(self):
        return self.winner != Player.BLANK

    def empty_side(self):
        zerot = True
        add_scoret = 0
        for cupt in (self.sides[Player.TOP]):
            if (cupt.marbles != 0):
                zerot = False
                add_scoret += cupt.marbles
        zerob = True
        add_scoreb = 0
        for cupb in (self.sides[Player.BOTTOM]):
            if (cupb.marbles != 0):
                zerob = False
                add_scoreb += cupb.marbles
        if (zerot):
            return (Player.TOP, add_scoreb)
        if (zerob):
            self.score[Player.TOP] = self.score[Player.TOP] + add_scoreb
            return (Player.BOTTOM, add_scoret)
        return (Player.BLANK, 0)

    def after_move(self, last):
        # check if any side has all empty
        # if so declare the winner
        empty_side = self.empty_side()
        if (empty_side[0] != Player.BLANK):
            if (empty_side[0] == Player.TOP):
                self.score[Player.BOTTOM] = self.score[Player.BOTTOM] + \
                    empty_side[1]
            if (empty_side[0] == Player.BOTTOM):
                self.score[Player.TOP] = self.score[Player.TOP] + empty_side[1]
            if (self.score[Player.BOTTOM] > self.score[Player.TOP]):
                self.winner = Player.BOTTOM
            else:
                self.winner = Player.TOP

        opp = self.turn.opponent()
        # if the last cup a marble was placed in was empty then it takes opposing
        if (last[0] == "turn"):
            last_id = last[1]
            last_cup = self.get_cup_by_id(self.turn, last_id)
            if (last_cup.marbles == 1):
                opp_cup_id = N_COLS - last_id - 1
                opp_cup: Cup = self.sides[opp][opp_cup_id]
                opp_marbles = opp_cup.marbles
                # empty the last cup
                self.sides[self.turn][last[1]] = Cup(
                    self.turn, last_id, 0)
                # add the marbles to the store
                self.stores[self.turn] = Store(
                    self.turn, self.stores[self.turn].score+1+opp_marbles)
                # empty the opponents cup
                self.sides[opp][opp_cup_id] = Cup(opp, opp_cup_id, 0)

        # Switch turn
        self.turn = opp
        # if the last cup was the store then goes again
        if (last[0] == "store"):
            self.turn = self.turn.opponent()

    def move_marbles(self, cup_id: int):
        # moves the marbles from cup_id and returns the last cup a marble is dropped
        # returns the tuple specifying what side/store it lands on, the cup number on that side

        # check if cup has marbles maybe
        # check if valid move?
        # empty the cup and add 1 to every following possible cup/store
        # start_cup = cup.get_col()
        start_cup = self.get_cup_by_id(self.turn, cup_id)
        num_marbles = start_cup.get_marbles()
        self.sides[self.turn][cup_id] = Cup(self.turn, cup_id, 0)

        # if (self.turn == Player.BOTTOM):
        #     opp_count = 0
        #     for i in range(start_cup, start_cup+num_marbles):
        #         if (i < N_COLS):
        #             self.sides[Player.BOTTOM][i] = Cup(
        #                 Player.BOTTOM, i, self.sides[Player.BOTTOM][i].get_marbles()+1)
        #         elif (i > N_COLS):  # else it goes into top players side
        #             self.sides[Player.TOP][i] = Cup(
        #                 Player.TOP, opp_count, self.sides[Player.TOP][opp_count].get_marbles()+1)
        #             opp_count += 1
        #         else:  # else the cup col number is equal to the store
        #             self.stores[Player.BOTTOM] = Store(
        #                 Player.BOTTOM, self.stores[Player.BOTTOM]+1)

# more general turn
        opp = self.turn.opponent()
        opp_count = 0
        curr = cup_id+1
        last_cup = ("turn", curr)
        for i in range(cup_id+1, cup_id+num_marbles+1):
            # print(str(curr) + " opp: " + str(opp_count))
            if (curr < N_COLS | (i >= N_COLS & opp_count >= N_COLS)):
                # if curr is greater than or equal to 6 and opp_count is greater than 6 too
                # means it already went around both sides and is back to self.turn's row
                # so set it back to first cup of turn and also opp to 0 in case it goes
                # back to the opposing turn's side
                if (curr >= N_COLS):
                    curr = 0
                    opp_count = 0
                self.sides[self.turn][curr] = Cup(
                    self.turn, curr, self.sides[self.turn][curr].get_marbles()+1)
                last_cup = ("turn", curr)
                curr += 1
            elif (i > N_COLS):  # else it goes into top players side
                if (opp_count < N_COLS):
                    self.sides[opp][opp_count] = Cup(
                        opp, opp_count, self.sides[opp][opp_count].get_marbles()+1)
                    last_cup = ("opp", opp_count)
                    opp_count += 1
                else:  # go back to start of turn's row, not sure needed here anymore
                    # taken care of in first if
                    opp_count = 0
            else:  # else the cup col number is equal to the store
                if (curr == N_COLS):  # necessary if?
                    self.stores[self.turn] = Store(
                        self.turn, self.stores[self.turn].score+1)
                    last_cup = ("store", 0)
            # print(last_cup[0])
        return last_cup

        # in a post turn function, check if the whole side of a player is empty
        # then it's end of the game
        # in a post turn, if end marbles in store, that person goes again
        #  if last marble lands in an empty cup, that person takes the opposing cup too
