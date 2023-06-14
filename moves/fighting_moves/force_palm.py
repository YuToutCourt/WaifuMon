from ..move import Move
from waifu_types.type import Type

class ForcePalm(Move):
    def __init__(self):
        super().__init__("Force Palm", type=Type.FIGHTING, power=60, accuracy=100, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
