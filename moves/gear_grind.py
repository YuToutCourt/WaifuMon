from .move import Move
from waifu_types.type import Type

class GearGrind(Move):
    def __init__(self):
        super().__init__("Gear Grind", type=Type.STEEL, power=50, accuracy=85, pp=15, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
