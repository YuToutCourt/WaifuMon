from .move import Move
from waifu_types.type import Type

class HydroCannon(Move):
    def __init__(self):
        super().__init__("Hydro Cannon", type=Type.WATER, power=150, accuracy=90, pp=5, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass
