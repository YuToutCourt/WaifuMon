from .move import Move
from waifu_types.type import Type

class PoisonPowder(Move):
    def __init__(self):
        super().__init__("Poison Powder", type=Type.POISON, power=0, accuracy=75, pp=35, proba_effect=100)

    def effect(self):
        """
        Poisons opponent.
        """
        pass
