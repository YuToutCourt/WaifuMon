from ..move import Move
from waifu_types.type import Type

class StoredPower(Move):
    def __init__(self):
        super().__init__("Stored Power", type=Type.PSYCHIC, power=20, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases when user's stats have been raised.
        """
        pass
