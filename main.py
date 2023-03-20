from kalaha.agents.agent import Agent

from kalaha.agents.human_agent import HumanAgent
from kalaha.agents.mcts_agent import MCTSAgent
from kalaha.agents.random_agent import RandomAgent
from kalaha.controller import Controller
from kalaha.agents.alpha_beta import AlphaBetaMinimaxAgent
from kalaha.agents.minimax_agent import MinimaxAgent

if __name__ == '__main__':
    N_COLS = 6

    agent_classes = [HumanAgent, MinimaxAgent,
                     AlphaBetaMinimaxAgent, MCTSAgent, RandomAgent]
    # for i in range(len(agent_classes)):
    #     print(str(agent_classes[i]))
    #     # this is just a fast and easy way of choosing. it can be changed in the future
    #     print(i, agent_classes[i])

    print("Select your players:")
    print("0 - Human Player")
    print("1 - Minimax Player")
    print("2 - AlphaBeta Minimax Player")
    print("3 - Monte Carlo Tree Search Player")
    print("4 - Random Generator")
    # agent_top: Agent = agent_classes[int(input("enter top agent"))]()  # instantiate object from selected class
    #agent_bottom: Agent = agent_classes[int(input("enter bottom player"))]()
    print("Choice for top player:")
    first_agent = int(input("> "))
    print("Choice for bottom player:")
    second_agent = int(input("> "))
    controller = Controller(
        N_COLS, agent_classes[first_agent](), agent_classes[second_agent]())
    controller.play()
