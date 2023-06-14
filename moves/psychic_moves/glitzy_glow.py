from ..move import Move
from waifu_types.type import Type

class GlitzyGlow(Move):
    def __init__(self):
        super().__init__("Glitzy Glow", type=Type.PSYCHIC, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Reduces damage from Special attacks.
        """
        pass
