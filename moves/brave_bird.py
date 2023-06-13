from .move import Move
from waifu_types.type import Type

class BraveBird(Move):
    def __init__(self):
        super().__init__("Brave Bird", type=Type.FLYING, power=120, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
