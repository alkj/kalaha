from kalaha.gamex import Kalaha, Player
from kalaha.human import HumanAgent
import kalaha.view as View


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

        View.draw_grid(self.game)

        curr = self.game.turn
        while self.game.winner == Player.BLANK:

            print("What cup would you like to pick up?")
            choice = int(input("> "))
            last = self.game.move_marbles(choice)
            View.draw_grid(self.game)
            self.game.after_move(last)

        print(f"Player {self.game.winner.name} Won!")

        return self.game.winner
