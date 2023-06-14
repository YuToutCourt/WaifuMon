from ..move import Move
from waifu_types.type import Type

class LuminaCrash(Move):
    def __init__(self):
        super().__init__("Lumina Crash", type=Type.PSYCHIC, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Harshly lowers target’s Special Defense.
        """
        pass
