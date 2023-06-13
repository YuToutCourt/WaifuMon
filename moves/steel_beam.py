from .move import Move
from waifu_types.type import Type

class SteelBeam(Move):
    def __init__(self):
        super().__init__("Steel Beam", type=Type.STEEL, power=140, accuracy=95, pp=5, proba_effect=100)

    def effect(self):
        """
        User loses 50% of its HP.
        """
        pass
