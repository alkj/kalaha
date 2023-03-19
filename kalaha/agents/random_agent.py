import random
from kalaha.agents.agent import Agent


class RandomAgent(Agent):
    def choose(self, input_game) -> int:
        choice = random.choice(input_game.get_possible_moves())
        print(self, "chooses:", choice, "for", input_game.current_player)
        return choice

    def __str__(self):
        return "Random Agent"
