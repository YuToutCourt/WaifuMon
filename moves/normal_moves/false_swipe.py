from ..move import Move
from waifu_types.type import Type

class FalseSwipe(Move):
    def __init__(self):
        super().__init__("False Swipe", type=Type.NORMAL, power=40, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Always leaves opponent with at least 1 HP.
        """
        pass