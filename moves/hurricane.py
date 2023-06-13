from .move import Move
from waifu_types.type import Type

class Hurricane(Move):
    def __init__(self):
        super().__init__("Hurricane", type=Type.FLYING, power=110, accuracy=70, pp=10, proba_effect=30)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
