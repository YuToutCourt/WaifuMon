from .move import Move
from waifu_types.type import Type

class Confusion(Move):
    def __init__(self):
        super().__init__("Confusion", type=Type.PSYCHIC, power=50, accuracy=100, pp=25, proba_effect=10)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
