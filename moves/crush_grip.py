from .move import Move
from waifu_types.type import Type

class CrushGrip(Move):
    def __init__(self):
        super().__init__("Crush Grip", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        More powerful when opponent has higher HP.
        """
        pass
