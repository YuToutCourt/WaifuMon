from .move import Move
from waifu_types.type import Type

class TeeterDance(Move):
    def __init__(self):
        super().__init__("Teeter Dance", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Confuses all Pok�mon.
        """
        pass
