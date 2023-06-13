from .move import Move
from waifu_types.type import Type

class ShadowClaw(Move):
    def __init__(self):
        super().__init__("Shadow Claw", type=Type.GHOST, power=70, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
