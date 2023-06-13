from .move import Move
from waifu_types.type import Type

class BehemothBlade(Move):
    def __init__(self):
        super().__init__("Behemoth Blade", type=Type.STEEL, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Damage doubles if target is Dynamaxed.
        """
        pass
