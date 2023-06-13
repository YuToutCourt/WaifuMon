from .move import Move
from waifu_types.type import Type

class Double-Edge(Move):
    def __init__(self):
        super().__init__("Double-Edge", type=Type.NORMAL, power=120, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
