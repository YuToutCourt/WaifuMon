from ..move import Move
from waifu_types.type import Type

class Mud-Slap(Move):
    def __init__(self):
        super().__init__("Mud-Slap", type=Type.GROUND, power=20, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass
