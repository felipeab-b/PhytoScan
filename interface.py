from abc import ABC, abstractmethod

class ITerrain(ABC):

    @abstractmethod
    def get_root(self):
        pass

    @abstractmethod
    def free_spaces(self, x, y):
        pass

    @abstractmethod
    def add_root(self, x, y):
        pass