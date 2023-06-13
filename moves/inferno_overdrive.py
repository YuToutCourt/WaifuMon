from .move import Move
from waifu_types.type import Type

class InfernoOverdrive(Move):
    def __init__(self):
        super().__init__("Inferno Overdrive", type=Type.FIRE, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Fire type Z-Move.
        """
        pass
