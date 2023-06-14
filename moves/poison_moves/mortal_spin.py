from ..move import Move
from waifu_types.type import Type

class MortalSpin(Move):
    def __init__(self):
        super().__init__("Mortal Spin", type=Type.POISON, power=30, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Removes entry hazards and trap move effects, and poisons opposing Pokémon.
        """
        pass
