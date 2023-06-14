from ..move import Move
from waifu_types.type import Type

class BoneRush(Move):
    def __init__(self):
        super().__init__("Bone Rush", type=Type.GROUND, power=25, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
