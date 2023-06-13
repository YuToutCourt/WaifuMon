from .move import Move
from waifu_types.type import Type

class GastroAcid(Move):
    def __init__(self):
        super().__init__("Gastro Acid", type=Type.POISON, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Cancels out the effect of the opponent's Ability.
        """
        pass
