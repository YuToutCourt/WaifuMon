from ..move import Move
from waifu_types.type import Type

class SplishySplash(Move):
    def __init__(self):
        super().__init__("Splishy Splash", type=Type.WATER, power=90, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
