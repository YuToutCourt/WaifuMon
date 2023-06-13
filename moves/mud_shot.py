from .move import Move
from waifu_types.type import Type

class MudShot(Move):
    def __init__(self):
        super().__init__("Mud Shot", type=Type.GROUND, power=55, accuracy=95, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
