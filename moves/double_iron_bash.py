from .move import Move
from waifu_types.type import Type

class DoubleIronBash(Move):
    def __init__(self):
        super().__init__("Double Iron Bash", type=Type.STEEL, power=60, accuracy=100, pp=5, proba_effect=30)

    def effect(self):
        """
        Hits twice in one turn; may cause flinching.
        """
        pass
