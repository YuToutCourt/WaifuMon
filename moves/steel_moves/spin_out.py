from ..move import Move
from waifu_types.type import Type

class SpinOut(Move):
    def __init__(self):
        super().__init__("Spin Out", type=Type.STEEL, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Harshly lowers user’s Speed.
        """
        pass
