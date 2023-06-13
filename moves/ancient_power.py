from .move import Move
from waifu_types.type import Type

class AncientPower(Move):
    def __init__(self):
        super().__init__("Ancient Power", type=Type.ROCK, power=60, accuracy=100, pp=5, proba_effect=10)

    def effect(self):
        """
        May raise all user's stats at once.
        """
        pass
