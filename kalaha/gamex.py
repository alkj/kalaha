# class Player
# class Cup
# class Store
# class Move
# class Kalaha
import string
from typing import Dict, List, Tuple, Optional, Union, Iterable
from enum import Enum

from kalaha.player import Player


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
        if self.col == self.cols and self.side == Player.BOTTOM:
            return Store(Player.BOTTOM)
        # if top player side and last cup
        elif self.col == 0 and self.side == Player.TOP:
            return Store(Player.TOP)
        # if any bottom player's cup
        elif self.side == Player.BOTTOM:
            return Cup(self.side, self.col + 1)
        # else any top player's cup
        else:
            return Cup(self.side, self.col - 1)

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


class Kalaha:
    """
    The game state
    """

    def __init__(self, cols):
        self.cols = cols
        self.turn: Player = Player.BOTTOM
        self.sides = {
            Player.TOP: [Cup(Player.TOP, i, 4) for i in range(self.cols)],
            Player.BOTTOM: [Cup(Player.BOTTOM, i, 4) for i in range(self.cols)]
        }
        # self.sides = {
        #     Player.TOP: [Cup(Player.TOP, 0), Cup(Player.TOP, 1)],
        #     Player.BOTTOM: [Cup(Player.BOTTOM, i) for i in range(N_COLS)]
        # }
        self.stores = {
            Player.TOP: Store(Player.TOP, 0),
            Player.BOTTOM: Store(Player.BOTTOM, 0)
        }
        # self.score = {Player.TOP: self.stores[Player.TOP].score,
        #               Player.BOTTOM: self.stores[Player.BOTTOM].score}
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

    def is_valid(self, choice: int):
        # check that the input choice is valid, can move that cell
        if (choice < 0 or choice > 5):
            return (False)
        elif (self.sides[self.turn][choice].get_marbles() <= 0):
            return (False)
        else:
            return (True)

    def did_steal(self, last):
        opp = self.turn.opponent()
        # if the last cup a marble was placed in was empty then it takes opposing
        if (last[0] == "turn"):  # if lands on current player's side
            last_id = last[1]
            last_cup = self.get_cup_by_id(self.turn, last_id)

            # get the opposing players cup
            opp_cup_id = self.cols - last_id - 1
            opp_cup: Cup = self.sides[opp][opp_cup_id]
            opp_marbles = opp_cup.marbles

            # if lands in empty cup and opposite cup is not empty
            if (last_cup.marbles == 1 and opp_marbles > 0):
                # empty the last cup
                self.sides[self.turn][last[1]] = Cup(
                    self.turn, last_id, 0)
                # add the marbles to the store
                self.stores[self.turn] = Store(
                    self.turn, self.stores[self.turn].score + 1 + opp_marbles)
                # empty the opponents cup
                self.sides[opp][opp_cup_id] = Cup(opp, opp_cup_id, 0)
                self.score[self.turn] = self.stores[self.turn].score
                return True

        else:
            return False

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
        # Switch turn
        self.turn = opp
        # if the last cup was the store then goes again
        if (last[0] == "store"):
            self.turn = self.turn.opponent()
            print("Last marble landed in your store. Go again!")

    def move_marbles(self, cup_id: int) -> (string, int):
        # moves the marbles from cup_id and returns the last cup a marble is dropped
        # returns the tuple specifying what side/store it lands on, the cup number on that side

        # check if cup has marbles maybe
        # check if valid move?
        # empty the cup and add 1 to every following possible cup/store
        # start_cup = cup.get_col()
        start_cup = self.get_cup_by_id(self.turn, cup_id)
        num_marbles = start_cup.get_marbles()
        self.sides[self.turn][cup_id] = Cup(self.turn, cup_id, 0)

        # more general turn
        opp = self.turn.opponent()
        opp_count = 0
        curr = cup_id + 1
        last_cup = ("turn", curr)
        for i in range(cup_id + 1, cup_id + num_marbles + 1):
            # print(str(curr) + " opp: " + str(opp_count))
            if curr < self.cols or (i >= self.cols & opp_count >= self.cols):
                # if curr is greater than or equal to 6 and opp_count is greater than 6 too
                # means it already went around both sides and is back to self.turn's row
                # so set it back to first cup of turn and also opp to 0 in case it goes
                # back to the opposing turn's side
                if (curr >= self.cols):
                    curr = 0
                    opp_count = 0
                self.sides[self.turn][curr] = Cup(
                    self.turn, curr, self.sides[self.turn][curr].get_marbles() + 1)
                last_cup = ("turn", curr)
                curr += 1
            elif (i > self.cols):  # else it goes into top players side
                if (opp_count < self.cols):
                    self.sides[opp][opp_count] = Cup(
                        opp, opp_count, self.sides[opp][opp_count].get_marbles() + 1)
                    last_cup = ("opp", opp_count)
                    opp_count += 1
                else:  # go back to start of turn's row, not sure needed here anymore
                    # taken care of in first if
                    opp_count = 0
            else:  # else the cup col number is equal to the store
                if (curr == self.cols):  # necessary if?
                    self.stores[self.turn] = Store(
                        self.turn, self.stores[self.turn].score + 1)
                    last_cup = ("store", 0)
            # print(last_cup[0])
        return last_cup

        # in a post turn function, check if the whole side of a player is empty
        # then it's end of the game
        # in a post turn, if end marbles in store, that person goes again
        #  if last marble lands in an empty cup, that person takes the opposing cup too
        # need to revise steal, steals at the very end when there's just 1's moving around
        #    and should not be stealing

    def get_possible_moves(self):
        moves = []
        for i in self.sides[self.turn]:
            if i.marbles != 0:
                moves.append(i.col)
        return moves

    def get_score(self):
        return self.stores[Player.TOP].score - self.stores[Player.BOTTOM].score

    def __str__(self):

        border = "--" * (self.cols * 2)
        row_separator = "  " + "--" * self.cols

        returned_string = "    5 4 3 2 1 0\n"
        returned_string = returned_string + border + "\n"

        top = "    "
        for cupt in reversed(self.sides[Player.TOP]):
            top += str(cupt.marbles) + " "
        returned_string = returned_string + top + "\n"
        stores = str(self.stores[Player.TOP].score) + \
                 row_separator + " " + str(self.stores[Player.BOTTOM].score)
        returned_string = returned_string + stores + "\n"
        bottom = "    "
        for cupb in self.sides[Player.BOTTOM]:
            bottom += str(cupb.marbles) + " "
        returned_string = returned_string + bottom + "\n"

        returned_string = returned_string + border + "\n"
        returned_string = returned_string + "    0 1 2 3 4 5\n"
        return returned_string + "\n"
