from ..move import Move
from waifu_types.type import Type

class MistyExplosion(Move):
    def __init__(self):
        super().__init__("Misty Explosion", type=Type.FAIRY, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases on Misty Terrain.
        """
        pass
