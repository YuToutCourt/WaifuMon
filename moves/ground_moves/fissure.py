from ..move import Move
from waifu_types.type import Type

class Fissure(Move):
    def __init__(self):
        super().__init__("Fissure", type=Type.GROUND, power=0, accuracy=30, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        One-Hit-KO, if it hits.
        """
        pass
