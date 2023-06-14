from ..move import Move
from waifu_types.type import Type

class NaturalGift(Move):
    def __init__(self):
        super().__init__("Natural Gift", type=Type.NORMAL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Power and type depend on the user's held berry.
        """
        pass
