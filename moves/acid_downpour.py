from .move import Move
from waifu_types.type import Type

class AcidDownpour(Move):
    def __init__(self):
        super().__init__("Acid Downpour", type=Type.POISON, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Poison type Z-Move.
        """
        pass
