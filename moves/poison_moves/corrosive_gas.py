from ..move import Move
from waifu_types.type import Type

class CorrosiveGas(Move):
    def __init__(self):
        super().__init__("Corrosive Gas", type=Type.POISON, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Removes opponent's items.
        """
        pass
