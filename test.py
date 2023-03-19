from kalaha.agents.mcts_agent_2 import MCTSAgent2
from kalaha.agents.alpha_beta import AlphaBetaMinimaxAgent
from kalaha.controller import Controller
from kalaha.player import Player

if __name__ == '__main__':
    N_COLS = 6
    agents = {
        Player.TOP: AlphaBetaMinimaxAgent(),
        Player.BOTTOM: MCTSAgent2()
    }
    controller = Controller(N_COLS, agents)

    controller.game.sides[Player.BOTTOM][0].marbles = 6
    controller.game.sides[Player.BOTTOM][1].marbles = 4
    controller.game.sides[Player.BOTTOM][2].marbles = 2
    controller.game.sides[Player.BOTTOM][3].marbles = 3
    controller.game.sides[Player.BOTTOM][4].marbles = 1
    controller.game.sides[Player.BOTTOM][5].marbles = 1

    controller.play()
