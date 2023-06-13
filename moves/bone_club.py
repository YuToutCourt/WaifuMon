from .move import Move
from waifu_types.type import Type

class BoneClub(Move):
    def __init__(self):
        super().__init__("Bone Club", type=Type.GROUND, power=65, accuracy=85, pp=20, proba_effect=10)

    def effect(self):
        """
        May cause flinching.
        """
        pass
