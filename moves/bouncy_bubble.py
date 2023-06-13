from .move import Move
from waifu_types.type import Type

class BouncyBubble(Move):
    def __init__(self):
        super().__init__("Bouncy Bubble", type=Type.WATER, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass
