from .move import Move
from waifu_types.type import Type

class DefendOrder(Move):
    def __init__(self):
        super().__init__("Defend Order", type=Type.BUG, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises user's Defense and Special Defense.
        """
        pass
