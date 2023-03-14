from kalaha.gamex import Kalaha, Cup, Player
import kalaha.gamex as Game

row_separator = "  " + "--" * Game.N_COLS
border = "--" * (Game.N_COLS * 2)


def draw(game: Kalaha):
    print("    5 4 3 2 1 0")
    print(border)
    top = "    "
    for cupt in reversed(game.sides[Player.TOP]):
        top += str(cupt.marbles) + " "
    print(top)
    stores = str(game.stores[Player.TOP].score) + \
        row_separator + " " + str(game.stores[Player.BOTTOM].score)
    print(stores)
    bottom = "    "
    for cupb in game.sides[Player.BOTTOM]:
        bottom += str(cupb.marbles) + " "
    print(bottom)
    print(border)
    print("    0 1 2 3 4 5")

    print()


# next steps
# draw out the correct board, showing marble in cups x
# get controller somewhat going x
# actions
# out of bounds, entering invalid spots
# putting indexes on the board
# determining the end of the game
# displaying the score throughout the game
# steal, go again, move as actions? not just after a move function
