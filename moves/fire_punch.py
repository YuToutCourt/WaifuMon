from .move import Move
from waifu_types.type import Type

class FirePunch(Move):
    def __init__(self):
        super().__init__("Fire Punch", type=Type.FIRE, power=75, accuracy=100, pp=15, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
