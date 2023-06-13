from .move import Move
from waifu_types.type import Type

class PayDay(Move):
    def __init__(self):
        super().__init__("Pay Day", type=Type.NORMAL, power=40, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Money is earned after the battle.
        """
        pass
