from abc import abstractmethod



class Agent:
    @abstractmethod
    def choose(self, game) -> int:
        pass

    @abstractmethod
    def __str__(self):
        pass
