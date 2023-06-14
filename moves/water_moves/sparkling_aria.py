from ..move import Move
from waifu_types.type import Type

class SparklingAria(Move):
    def __init__(self):
        super().__init__("Sparkling Aria", type=Type.WATER, power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Heals the burns of its target.
        """
        pass
