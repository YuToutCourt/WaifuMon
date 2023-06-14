from ..move import Move
from waifu_types.type import Type

class Will-O-Wisp(Move):
    def __init__(self):
        super().__init__("Will-O-Wisp", type=Type.FIRE, power=0, accuracy=85, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Burns opponent.
        """
        pass
