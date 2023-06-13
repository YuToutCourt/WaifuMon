from .move import Move
from waifu_types.type import Type

class Thunder(Move):
    def __init__(self):
        super().__init__("Thunder", type=Type.ELECTRIC, power=110, accuracy=70, pp=10, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
