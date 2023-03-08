from game import Game

if __name__ == '__main__':
    g = Game()
    print(g.__str__())
    g.moveMarble(4)  # RED TURN
    print(g.__str__())
    g.moveMarble(3)  # BLACK TURN
    print(g.__str__())
    g.moveMarble(2)  # RED TURN
    print(g.__str__())
    g.moveMarble(5)  # BLACK TURN
    print(g.__str__())
