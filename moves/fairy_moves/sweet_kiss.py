from ..move import Move
from waifu_types.type import Type

class SweetKiss(Move):
    def __init__(self):
        super().__init__("Sweet Kiss", type=Type.FAIRY, power=0, accuracy=75, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
