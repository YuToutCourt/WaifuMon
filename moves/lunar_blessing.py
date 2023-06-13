from .move import Move
from waifu_types.type import Type

class LunarBlessing(Move):
    def __init__(self):
        super().__init__("Lunar Blessing", type=Type.PSYCHIC, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Heals user's status conditions and recovers HP.
        """
        pass
