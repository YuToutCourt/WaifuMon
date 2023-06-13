from .move import Move
from waifu_types.type import Type

class SpeedSwap(Move):
    def __init__(self):
        super().__init__("Speed Swap", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user exchanges Speed stats with the target.
        """
        pass
