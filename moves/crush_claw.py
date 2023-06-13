from .move import Move
from waifu_types.type import Type

class CrushClaw(Move):
    def __init__(self):
        super().__init__("Crush Claw", type=Type.NORMAL, power=75, accuracy=95, pp=10, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
