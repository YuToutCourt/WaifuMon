from ..move import Move
from waifu_types.type import Type

class GigavoltHavoc(Move):
    def __init__(self):
        super().__init__("Gigavolt Havoc", type=Type.ELECTRIC, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Electric type Z-Move.
        """
        pass
