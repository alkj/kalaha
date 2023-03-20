from kalaha.agents.alpha_beta import AlphaBetaMinimaxAgent
from kalaha.agents.human_agent import HumanAgent
from kalaha.agents.mcts_agent import MCTSAgent
from kalaha.agents.mcts_agent_2 import MCTSAgent2
from kalaha.agents.minimax_agent import MinimaxAgent
from kalaha.agents.random_agent import RandomAgent
from kalaha.controller import Controller

if __name__ == '__main__':
    N_COLS = 6

    agent_classes = [HumanAgent, MinimaxAgent,
                     AlphaBetaMinimaxAgent, MCTSAgent,
                     RandomAgent, MCTSAgent2]

    print("Select your players:")
    print("0 - Human Player")
    print("1 - Minimax Player")
    print("2 - AlphaBeta Minimax Player")
    print("3 - Monte Carlo Tree Search Player")
    print("4 - Random Generator")
    print("5 - MCTS Player with another implementation")

    print("Choice for top player:")
    first_agent = int(input("> "))
    print("Choice for bottom player:")
    second_agent = int(input("> "))
    controller = Controller(
        N_COLS, agent_classes[first_agent](), agent_classes[second_agent]())
    controller.play()
