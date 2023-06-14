from ..move import Move
from waifu_types.type import Type

class LaserFocus(Move):
    def __init__(self):
        super().__init__("Laser Focus", type=Type.NORMAL, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        User's next attack is guaranteed to result in a critical hit.
        """
        pass
