from ..move import Move
from waifu_types.type import Type

class AcidArmor(Move):
    def __init__(self):
        super().__init__("Acid Armor", type=Type.POISON, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Defense.
        """
        pass
