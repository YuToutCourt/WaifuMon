from .move import Move
from waifu_types.type import Type

class PoisonGas(Move):
    def __init__(self):
        super().__init__("Poison Gas", type=Type.POISON, power=0, accuracy=90, pp=40, proba_effect=100)

    def effect(self):
        """
        Poisons opponent.
        """
        pass
