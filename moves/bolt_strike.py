from .move import Move
from waifu_types.type import Type

class BoltStrike(Move):
    def __init__(self):
        super().__init__("Bolt Strike", type=Type.ELECTRIC, power=130, accuracy=85, pp=5, proba_effect=20)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
