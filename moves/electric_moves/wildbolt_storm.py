from ..move import Move
from waifu_types.type import Type

class WildboltStorm(Move):
    def __init__(self):
        super().__init__("Wildbolt Storm", type=Type.ELECTRIC, power=100, accuracy=80, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        May paralyze target.
        """
        pass
