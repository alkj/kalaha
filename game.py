class Game:
    def __init__(self):
        self.red_player_turn: bool = False

        self.red_lane = [4] * 6
        self.black_lane = [4] * 6

        self.red_points = 0
        self.black_points = 0

    def __str__(self):
        game_string = "RED\n"
        for i in self.red_lane:
            game_string = game_string + " " + str(i)
        game_string = game_string + "\n" + str(self.red_points) + " " * 11 + str(self.black_points) + "\n"
        for i in self.black_lane:
            game_string = game_string + " " + str(i)
        game_string = game_string + "\nBLACK"
        return game_string

    def moveMarble(self, index: int):
        if self.red_player_turn:
            marbles_in_hand = self.red_lane[index]
            self.red_lane[index] = 0
            while index < 6:

                index = index + 1

        pass
