from .move import Move
from waifu_types.type import Type

class SilverWind(Move):
    def __init__(self):
        super().__init__("Silver Wind", type=Type.BUG, power=60, accuracy=100, pp=5, proba_effect=10)

    def effect(self):
        """
        May raise all stats of user at once.
        """
        pass
