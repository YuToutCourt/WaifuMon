from ..move import Move
from waifu_types.type import Type

class LifeDew(Move):
    def __init__(self):
        super().__init__("Life Dew", type=Type.WATER, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User and teammates recover HP.
        """
        pass
