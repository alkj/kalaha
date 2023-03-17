from kalaha.agent import Agent
from kalaha.gamex import Kalaha, Player
from kalaha.human_agent import HumanAgent


class Controller:
    """
    The controller requests moves to the agents (whetever their are human or AI) and applies it to the game
    """

    def __init__(self, cols):
        self.cols = cols
        self.game = Kalaha(self.cols)
        self.player_bottom: Agent = HumanAgent()
        self.player_top: Agent = HumanAgent()
        self.views = {Player.BOTTOM: self.player_bottom, Player.TOP: self.player_top}
        self.prev_turn = Player.BLANK
        self.current_player = self.player_bottom

    def play(self) -> Player:
        """
        Starts a game with the two agent and manages it till the end
        Don't call this method twice, but create a new controller with two
        new agents (Agents could be stateful)
        """

        print(self.game.__str__())

        while self.game.winner == Player.BLANK:
            choice = self.current_player.choose(self.game)
            if self.game.is_valid(choice):
                self.game.move_marbles(choice)
                print(self.game.__str__())
            else:
                print("That is not a valid choice, try again.")

        print(f"Player {self.game.winner.name} Won!")

        return self.game.winner
