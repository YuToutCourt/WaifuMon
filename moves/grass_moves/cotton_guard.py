from ..move import Move
from waifu_types.type import Type

class CottonGuard(Move):
    def __init__(self):
        super().__init__("Cotton Guard", type=Type.GRASS, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Drastically raises user's Defense.
        """
        pass