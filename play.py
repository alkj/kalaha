from kalaha.gamex import Kalaha, Player
from kalaha.controller import Controller
from kalaha.human import HumanAgent
import sys


def menu():
    print("Human vs. Human Mancala")
    # choice = int(input("> "))
    human1 = HumanAgent(Kalaha, Player.TOP)
    human2 = HumanAgent(Kalaha, Player.BOTTOM)
    controller = Controller(Kalaha, human1, human2)
    controller.play()


if __name__ == "__main__":
    while True:
        menu()
