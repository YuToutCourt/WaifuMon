from abc import ABC, abstractmethod
from wtypes.type import Type

class Move(ABC):
    def __init__(self, name:str, type:Type, power:int, accuracy:int, pp:int, priority:int, 
                 proba_effect=100):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority
        self.proba_effect = proba_effect
        self.waif_user = None
        self.waifu_reciver = None

    def set_waif_user(self, waif_user):
        self.waif_user = waif_user
        
    def set_waifu_reciver(self, waifu_reciver):
        self.waifu_reciver = waifu_reciver

    @abstractmethod
    def effect(self):
        pass