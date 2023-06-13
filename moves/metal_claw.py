from .move import Move
from waifu_types.type import Type

class MetalClaw(Move):
    def __init__(self):
        super().__init__("Metal Claw", type=Type.STEEL, power=50, accuracy=95, pp=35, proba_effect=10)

    def effect(self):
        """
        May raise user's Attack.
        """
        pass
