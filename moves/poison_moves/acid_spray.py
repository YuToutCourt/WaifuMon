from ..move import Move
from waifu_types.type import Type

class AcidSpray(Move):
    def __init__(self):
        super().__init__("Acid Spray", type=Type.POISON, power=40, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Special Defense.
        """
        pass
