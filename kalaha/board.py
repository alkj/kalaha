from kalaha.gamex import Kalaha, Cup, Player
import kalaha.gamex as Game

row_separator = "  " + "--" * Game.N_COLS


def draw(game: Kalaha):

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
