from .move import Move
from waifu_types.type import Type

class TakeHeart(Move):
    def __init__(self):
        super().__init__("Take Heart", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Heals user's status conditions and raises its stats.
        """
        pass
