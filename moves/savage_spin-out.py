from .move import Move
from waifu_types.type import Type

class SavageSpin-Out(Move):
    def __init__(self):
        super().__init__("Savage Spin-Out", type=Type.BUG, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Bug type Z-Move.
        """
        pass
