from enum import Enum


class Player(Enum):
    BOTTOM = 0
    TOP = 1
    BLANK = -1

    def store(self):
        """
        Returns the store that marbles of the given player have to reach to score a point
        """
        if self == Player.BOTTOM:
            return N_COLS
        elif self == Player.TOP:
            return 0
        else:
            raise ValueError("Blank player has no goal coordinates")

    def opponent(self):
        """
        Returns the opponent Player object
        """
        if self == Player.BOTTOM:
            return Player.TOP
        elif self == Player.TOP:
            return Player.BOTTOM
        else:
            raise ValueError("Blank player has no opponents")

    def is_empty(self):
        return self == Player.BLANK

    def is_player(self):
        return self != Player.BLANK

    def get_repr(self):
        if self == Player.BOTTOM:
            return "B"
        elif self == Player.TOP:
            return "T"
        else:
            return "NA"
