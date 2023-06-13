from .move import Move
from waifu_types.type import Type

class FlareBlitz(Move):
    def __init__(self):
        super().__init__("Flare Blitz", type=Type.FIRE, power=120, accuracy=100, pp=15, proba_effect=10)

    def effect(self):
        """
        User receives recoil damage. May burn opponent.
        """
        pass
