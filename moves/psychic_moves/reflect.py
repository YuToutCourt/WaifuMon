from ..move import Move
from waifu_types.type import Type

class Reflect(Move):
    def __init__(self):
        super().__init__("Reflect", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves damage from Physical attacks for 5 turns.
        """
        pass
