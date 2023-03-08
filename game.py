class Game:
    def __init__(self):
        self.is_red_player_turn: bool = True

        self.marbles_in_hand = 0

        self.red_lane = [4] * 6
        self.black_lane = [4] * 6

        self.current_lane = self.red_lane

        self.red_points = 0
        self.black_points = 0

    def __str__(self):
        game_string = "RED\n"
        red_lane = self.red_lane.copy()
        red_lane.reverse()
        for i in red_lane:
            game_string = game_string + " " + str(i)
        game_string = game_string + "\n" + str(self.red_points) + " " * 11 + str(self.black_points) + "\n"
        for i in self.black_lane:
            game_string = game_string + " " + str(i)
        game_string = game_string + "\nBLACK"
        return game_string

    def change_lane(self):
        if self.current_lane == self.red_lane:
            self.current_lane = self.black_lane
        else:
            self.current_lane = self.red_lane

    def moveMarble(self, index: int):
        if self.is_red_player_turn:
            self.current_lane = self.red_lane
        else:
            self.current_lane = self.black_lane

        self.marbles_in_hand = self.current_lane[index]
        self.current_lane[index] = 0
        while True:
            if self.marbles_in_hand <= 0:
                self.is_red_player_turn = not self.is_red_player_turn
                break
            index = index + 1
            if index >= 6:
                index = 0
                if self.is_red_player_turn and self.current_lane == self.red_lane:
                    self.red_points = self.red_points + 1
                    self.marbles_in_hand = self.marbles_in_hand - 1
                if not self.is_red_player_turn and self.current_lane == self.black_lane:
                    self.black_points = self.black_points + 1
                    self.marbles_in_hand = self.marbles_in_hand - 1
                self.change_lane()
            self.current_lane[index] = self.current_lane[index] + 1
            self.marbles_in_hand = self.marbles_in_hand - 1
