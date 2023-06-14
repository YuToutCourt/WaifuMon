from ..move import Move
from waifu_types.type import Type

class Quash(Move):
    def __init__(self):
        super().__init__("Quash", type=Type.DARK, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Makes the target act last this turn.
        """
        pass
