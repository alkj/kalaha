import copy
import random

from kalaha.agents.agent import Agent
from kalaha.player import Player


class Node:
    def __init__(self, prior, game):
        self.prior = prior
        self.game = game

        self.children = []
        self.visit_count = 0
        self.value_sum = 0
        self.state = None

    def value(self):
        return self.value_sum / self.visit_count


class MCTSAgent2(Agent):

    def __init__(self):
        self.max_depth = 2

    """
    An human agent providing a CLI to choose the moves
    """

    def choose(self, input_game) -> int:
        choice = self.mcts(copy.deepcopy(input_game), 0)
        print(self, "chooses:", choice, "for", input_game.current_player)
        return choice

    def mcts(self, input_game, depth: int) -> int:

        best_move = -1

        game = copy.deepcopy(input_game)

        # the top player wants to maximize the score of the board
        if game.current_player == Player.TOP:
            maximum_score = -48
            for i in game.get_possible_moves():
                # print("checking move ", i)
                game_copy = copy.deepcopy(game)
                game_copy.move_marbles(i)
                # if the player after the move is the top player again, then the score should be maximized
                if game_copy.current_player == Player.TOP:
                    score = self.maximize(game_copy, depth + 1)
                    if score >= maximum_score:
                        maximum_score = score
                        best_move = i

                else:
                    score = self.minimize(game_copy, depth + 1)
                    if score >= maximum_score:
                        maximum_score = score
                        best_move = i
            #  print("maximum score:", maximum_score)

        else:  # bottom player
            minimum_score = 48
            for i in game.get_possible_moves():
                # print("checking move ", i)
                game_copy = copy.deepcopy(game)
                game_copy.move_marbles(i)
                if game_copy.current_player == Player.TOP:
                    score = self.maximize(game_copy, depth + 1)
                    if score <= minimum_score:
                        minimum_score = score
                        best_move = i
                else:
                    score = self.minimize(game_copy, depth + 1)
                    if score <= minimum_score:
                        minimum_score = score
                        best_move = i
            #  print("minimum score:", minimum_score)
        return best_move

    def minimize(self, input_game, depth: int) -> float:
        if input_game.winner == Player.TOP:
            return 1
        if input_game.winner == Player.BOTTOM:
            return 0
        if input_game.winner is None:
            return 0.5
        if depth == self.max_depth:  # run simulations
            simulations = []
            for i in range(10):
                simulations.append(self.simulate(input_game))
            return sum(simulations) / len(simulations)  # average win rate for top player

        minimum_score = 48

        game = copy.deepcopy(input_game)
        for i in game.get_possible_moves():
            game_copy = copy.deepcopy(game)
            game_copy.move_marbles(i)
            if game_copy.current_player == Player.TOP:
                score = self.maximize(game_copy, depth + 1)
            else:
                score = self.minimize(game_copy, depth + 1)
            if score <= minimum_score:
                minimum_score = score
        return minimum_score

    def maximize(self, input_game, depth: int) -> float:
        if input_game.winner == Player.TOP:
            return 1
        if input_game.winner == Player.BOTTOM:
            return 0
        if input_game.winner is None:
            return 0.5
        if depth == self.max_depth:
            simulations = []
            for i in range(10):
                simulations.append(self.simulate(input_game))
            return sum(simulations) / len(simulations)

        maximum_score = -48

        game = copy.deepcopy(input_game)
        simulations = []
        for i in game.get_possible_moves():
            game_copy = copy.deepcopy(game)
            game_copy.move_marbles(i)
            if game_copy.current_player == Player.TOP:
                score = self.maximize(game_copy, depth + 1)
            else:
                score = self.minimize(game_copy, depth + 1)
            simulations.append(score)
        return sum(simulations) / len(simulations)

    def __str__(self):
        return "MCTS Agent 2"

    def simulate(self, input_game) -> int:
        if input_game.winner == Player.TOP:
            return 1
        if input_game.winner == Player.BOTTOM:
            return 0
        random_choice = random.choice(input_game.get_possible_moves())
        game_copy = copy.deepcopy(input_game)
        game_copy.move_marbles(random_choice)
        return self.simulate(game_copy)
