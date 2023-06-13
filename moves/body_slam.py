from .move import Move
from waifu_types.type import Type

class BodySlam(Move):
    def __init__(self):
        super().__init__("Body Slam", type=Type.NORMAL, power=85, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
