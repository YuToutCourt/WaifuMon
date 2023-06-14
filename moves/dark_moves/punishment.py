from ..move import Move
from waifu_types.type import Type

class Punishment(Move):
    def __init__(self):
        super().__init__("Punishment", type=Type.DARK, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases when opponent's stats have been raised.
        """
        pass
