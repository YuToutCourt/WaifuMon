from ..move import Move
from waifu_types.type import Type

class PlayNice(Move):
    def __init__(self):
        super().__init__("Play Nice", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Attack. Always hits.
        """
        pass
