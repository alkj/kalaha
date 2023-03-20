import copy
import math
import random

from kalaha.agents.agent import Agent
from kalaha.player import Player


class Node:
    def __init__(self, prior, game):
        self.prior = prior
        self.game = game
        self.children = {}
        self.visit_count = 0
        self.value_sum = 0
        self.state = None

    def value(self):
        return self.value_sum / self.visit_count

    def select_child(self):
        best_score = -48
        best_action = -1
        best_child = None

        for action, child in self.children.items():
            score = self.ubc_score(child)  # ucb_score(self, child)
            if score > best_score:
                best_score = score
                best_action = action
                best_child = child

        return best_action, best_child

    def expand(self, game, move_to_play, ):
        for c in self.game.get_possible_moves():
            game_copy = copy.deepcopy(c)
            game_copy.move_marbles(c)
            self.children[c] = Node(self.value_sum, make_move(game_copy, c))

    def is_expanded(self):
        return self.children != {}

    def ubc_score(self, child):
        prior_score = child.prior * math.sqrt(self.visit_count) / (child.visit_count + 1)
        return child.value() + prior_score

    def highest_value_choice(self):
        best_index = -1
        highest_score = -48
        for i, c in self.children:
            if c.value() > highest_score:
                highest_score = c.value()
                best_index = i
        return best_index


def simulate_times(game, param) -> float:
    simulations = list(map(lambda n: simulate(game), [0] * param))
    return sum(simulations)


def simulate(input_game):
    if input_game.winner == Player.TOP:
        return 1.0
    if input_game.winner == Player.BOTTOM:
        return 0.0
    if input_game.winner is None:  # it's a draw
        return 0.5
    if len(input_game.get_possible_moves()) == 0:
        print("empty")
    random_choice = random.choice(input_game.get_possible_moves())
    game_copy = copy.deepcopy(input_game)
    game_copy.move_marbles(random_choice)
    return simulate(game_copy)


def make_move(game, move):
    deepcopy = copy.deepcopy(game)
    deepcopy.move_marbles(move)
    return deepcopy


class MCTSAgent2(Agent):

    def __init__(self):
        self.root = None
        self.max_depth = 2

    """
    SELECTION
    EXPANSION
    SIMULATION
    UPDATE
    
    
    """

    def choose(self, input_game) -> int:
        choice = self.mcts(input_game).highest_value_choice()
        print(self, "chooses:", choice, "for", input_game.current_player)
        return choice

    def mcts(self, input_game, sampling=10, simulations=10) -> Node:

        self.root = Node(0, copy.deepcopy(input_game))
        moves = self.root.game.get_possible_moves()  # list of moves

        # Expansion
        for m in moves:
            self.root.children[m] = Node(0, make_move(self.root.game, m))

        # Simulation
        for child in self.root.children:
            self.root.children[child].value_sum += simulate_times(self.root.children[child].game, sampling)
            self.root.children[child].visit_count += sampling

        # Update
        for child in self.root.children:
            self.root.value_sum += self.root.children[child].value_sum
            self.root.visit_count += self.root.children[child].visit_count

        print(self.root.value())
        for child in self.root.children:
            print(self.root.children[child].value(), end=" : ")

        path = [self.root]

        for i in range(simulations):  # number of simulations
            node = self.root
            while node.is_expanded():
                move, child = self.root.select_child()
                path.append(child)
                node = child

            parent = path[-2]

            # is game finished ?
            # who is playing ?
            # can it be expanded ?
            if node.game.winner == Player.BLANK:
                moves = node.game.get_possible_moves()  # list of moves

                # Expansion
                for m in moves:
                    node.children[m] = Node(0, make_move(node.game, m))

                # Simulation
                for child in node.children:
                    node.children[child].value_sum += simulate_times(node.children[child].game, sampling)
                    node.children[child].visit_count += sampling

                # Update
                for child in node.children:
                    node.value_sum += node.children[child].value_sum
                    node.visit_count += node.children[child].visit_count

                self.backpropagate(path, node.value())
            else:
                # the game is over. either a win or a draw.
                win = 0
                if node.game.winner == Player.TOP:
                    win = 1
                self.backpropagate(path, win)

        return self.root

    def backpropagate(self, path, win):
        for node in reversed(path):
            node.value_sum += win
            node.visit_count += 1

    def simulate(self, input_game) -> int:
        if input_game.winner == Player.TOP:
            return 1
        if input_game.winner == Player.BOTTOM:
            return 0
        random_choice = random.choice(input_game.get_possible_moves())
        game_copy = copy.deepcopy(input_game)
        game_copy.move_marbles(random_choice)
        return self.simulate(game_copy)

    def __str__(self):
        return "MCTS Agent 2"
