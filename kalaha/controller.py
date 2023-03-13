from kalaha.gamex import Kalaha, Player
from kalaha.human import HumanAgent
import kalaha.board as Board


class Controller:
    """
    The controller requests moves to the agents (whetever their are human or AI) and applies it to the game
    """

    def __init__(self, game: Kalaha, player_bottom: HumanAgent, player_top: HumanAgent):
        self.game = Kalaha()
        self.views = {Player.BOTTOM: player_bottom, Player.TOP: player_top}

    def play(self) -> Player:
        """
        Starts a game with the two agent and manages it till the end
        Don't call this method twice, but create a new controller with two
        new agents (Agents could be stateful)
        """
        prev_turn = Player.BLANK
        prev_actions_list = []

        Board.draw(self.game)

        curr = self.game.turn
        while self.game.winner == Player.BLANK:

            print("What cup would you like to pick up?")
            choice = int(input("> "))
            if (self.game.before_move(choice)):
                last = self.game.move_marbles(choice)
                Board.draw(self.game)
                self.game.after_move(last)
            else:
                print("That is not a valid choice, try again.")

        print(f"Player {self.game.winner.name} Won!")

        return self.game.winner
