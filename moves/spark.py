from .move import Move
from waifu_types.type import Type

class Spark(Move):
    def __init__(self):
        super().__init__("Spark", type=Type.ELECTRIC, power=65, accuracy=100, pp=20, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
