from ..move import Move
from waifu_types.type import Type

class TailGlow(Move):
    def __init__(self):
        super().__init__("Tail Glow", type=Type.BUG, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Drastically raises user's Special Attack.
        """
        pass
