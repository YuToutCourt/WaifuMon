from abc import ABC, abstractmethod
from waifu_types.type import Type

class Move(ABC):
    def __init__(self, name:str, type:Type, power:int, accuracy:int, pp:int, proba_effect=100):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.proba_effect = proba_effect

    @abstractmethod
    def effect(self):
        pass