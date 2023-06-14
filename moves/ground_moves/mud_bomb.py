from ..move import Move
from waifu_types.type import Type

class MudBomb(Move):
    def __init__(self):
        super().__init__("Mud Bomb", type=Type.GROUND, power=65, accuracy=85, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
