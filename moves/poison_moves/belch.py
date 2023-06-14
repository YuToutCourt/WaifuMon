from ..move import Move
from waifu_types.type import Type

class Belch(Move):
    def __init__(self):
        super().__init__("Belch", type=Type.POISON, power=120, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User must have consumed a Berry.
        """
        pass
