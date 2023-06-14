from ..move import Move
from waifu_types.type import Type

class Toxic(Move):
    def __init__(self):
        super().__init__("Toxic", type=Type.POISON, power=0, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Badly poisons opponent.
        """
        pass
