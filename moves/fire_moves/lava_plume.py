from ..move import Move
from waifu_types.type import Type

class LavaPlume(Move):
    def __init__(self):
        super().__init__("Lava Plume", type=Type.FIRE, power=80, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
