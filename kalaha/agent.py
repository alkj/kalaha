from abc import abstractmethod

from kalaha.gamex import Kalaha


class Agent:
    @abstractmethod
    def choose(self, game: Kalaha) -> int:
        pass

    @abstractmethod
    def __str__(self):
        pass
