from .move import Move
from waifu_types.type import Type

class SuperFang(Move):
    def __init__(self):
        super().__init__("Super Fang", type=Type.NORMAL, power=0, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Always takes off half of the opponent's HP.
        """
        pass
