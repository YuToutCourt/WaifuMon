from ..move import Move
from waifu_types.type import Type

class SteelWing(Move):
    def __init__(self):
        super().__init__("Steel Wing", type=Type.STEEL, power=70, accuracy=90, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        May raise user's Defense.
        """
        pass
