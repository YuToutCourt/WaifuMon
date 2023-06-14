from ..move import Move
from waifu_types.type import Type

class SearingSunrazeSmash(Move):
    def __init__(self):
        super().__init__("Searing Sunraze Smash", type=Type.STEEL, power=200, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Solgaleo-exclusive Z-Move.
        """
        pass
