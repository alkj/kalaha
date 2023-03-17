from kalaha.agent import Agent
from kalaha.gamex import Kalaha


class HumanAgent(Agent):
    """
    An human agent providing a CLI to choose the moves
    """

    def choose(self, game: Kalaha) -> int:
        print(f"Player {game.current_player.name}'s turn")
        print("What cup would you like to pick up?")
        return int(input("> "))

    def __str__(self):
        return "Human Agent"
