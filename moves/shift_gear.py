from .move import Move
from waifu_types.type import Type

class ShiftGear(Move):
    def __init__(self):
        super().__init__("Shift Gear", type=Type.STEEL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and sharply raises Speed.
        """
        pass
