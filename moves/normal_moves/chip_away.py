from ..move import Move
from waifu_types.type import Type

class ChipAway(Move):
    def __init__(self):
        super().__init__("Chip Away", type=Type.NORMAL, power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores opponent's stat changes.
        """
        pass
