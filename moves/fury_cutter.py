from .move import Move
from waifu_types.type import Type

class FuryCutter(Move):
    def __init__(self):
        super().__init__("Fury Cutter", type=Type.BUG, power=40, accuracy=95, pp=20, proba_effect=100)

    def effect(self):
        """
        Power increases each turn.
        """
        pass
