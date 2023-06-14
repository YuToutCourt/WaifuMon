from ..move import Move
from waifu_types.type import Type

class Charm(Move):
    def __init__(self):
        super().__init__("Charm", type=Type.FAIRY, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Attack.
        """
        pass
