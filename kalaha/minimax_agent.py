import copy

from kalaha.agent import Agent
from kalaha.gamex import Kalaha
from kalaha.player import Player


class MinimaxAgent(Agent):
    """
    An human agent providing a CLI to choose the moves
    """

    def choose(self, input_game: Kalaha) -> int:
        return self.minimax(copy.deepcopy(input_game), 0)

    def minimax(self, input_game: Kalaha, depth: int) -> int:
        game = copy.deepcopy(input_game)
        for i in game.get_possible_moves():
            game_copy = copy.deepcopy(game)
            game_copy.move_marbles(i)
            self.minimax(game_copy, depth)

    def minimize(self, input_game: Kalaha, depth: int) -> int:
        if input_game.winner != Player.BLANK:
            return input_game.get_score()
        if depth == 3:
            return input_game.get_score()

        best_move = -1
        minimum_score = 48

        game = copy.deepcopy(input_game)
        for i in game.get_possible_moves():
            game_copy = copy.deepcopy(game)
            game_copy.move_marbles(i)
            score = self.maximize(game_copy, depth + 1)
            if score < minimum_score:
                minimum_score = score
                best_move = i
        return best_move

    def maximize(self, input_game: Kalaha, depth: int) -> int:
        if input_game.winner != Player.BLANK:
            return input_game.get_score()
        if depth == 3:
            return input_game.get_score()

        best_move = -1
        maximum_score = -48

        game = copy.deepcopy(input_game)
        for i in game.get_possible_moves():
            game_copy = copy.deepcopy(game)
            game_copy.move_marbles(i)
            score = self.minimize(game_copy, depth + 1)
            if score > maximum_score:
                maximum_score = score
                best_move = i
        return best_move

    def __str__(self):
        return "Minimax Agent"
