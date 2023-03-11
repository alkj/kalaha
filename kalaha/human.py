from kalaha.gamex import Player, Player, Kalaha
from typing import List
import kalaha.view as View


class HumanAgent():
    """
    An human agent providing a CLI to choose the moves
    """

    def __init__(self, game: Kalaha, player: Player):
        self.game = game  # game is available but not access
        self.player = player

    def choose(self):
        View.draw_grid(self.game)
        print(f"What cup would you like to choose?")

    def __str__(self):
        return "Human Agent"
