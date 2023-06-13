from .move import Move
from waifu_types.type import Type

class BulletPunch(Move):
    def __init__(self):
        super().__init__("Bullet Punch", type=Type.STEEL, power=40, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass
