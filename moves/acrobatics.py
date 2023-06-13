from .move import Move
from waifu_types.type import Type

class Acrobatics(Move):
    def __init__(self):
        super().__init__("Acrobatics", type=Type.FLYING, power=55, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Stronger when the user does not have a held item.
        """
        pass
