from .move import Move
from waifu_types.type import Type

class Round(Move):
    def __init__(self):
        super().__init__("Round", type=Type.NORMAL, power=60, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Power increases if teammates use it in the same turn.
        """
        pass
