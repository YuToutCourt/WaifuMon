from ..move import Move
from waifu_types.type import Type

class SaltCure(Move):
    def __init__(self):
        super().__init__("Salt Cure", type=Type.ROCK, power=40, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage each turn; Steel and Water types are more affected.
        """
        pass
