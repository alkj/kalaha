from kalaha.agents.agent import Agent

from kalaha.agents.human_agent import HumanAgent
from kalaha.agents.mcts_agent import MCTSAgent
from kalaha.agents.random_agent import RandomAgent
from kalaha.controller import Controller
from kalaha.agents.alpha_beta import AlphaBetaMinimaxAgent
from kalaha.agents.minimax_agent import MinimaxAgent

if __name__ == '__main__':
    N_COLS = 6

    agent_classes = [HumanAgent, MinimaxAgent, AlphaBetaMinimaxAgent, MCTSAgent, RandomAgent]
    for i in range(len(agent_classes)):
        print(i, agent_classes[i])  # this is just a fast and easy way of choosing. it can be changed in the future
    #agent_top: Agent = agent_classes[int(input("enter top agent"))]()  # instantiate object from selected class
    #agent_bottom: Agent = agent_classes[int(input("enter bottom player"))]()

    controller = Controller(N_COLS, agent_classes[1](), agent_classes[3]())
    controller.play()
