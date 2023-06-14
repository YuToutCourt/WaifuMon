from ..move import Move
from waifu_types.type import Type

class Pounce(Move):
    def __init__(self):
        super().__init__("Pounce", type=Type.BUG, power=50, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
