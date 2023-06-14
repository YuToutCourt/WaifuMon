from ..move import Move
from waifu_types.type import Type

class BulkUp(Move):
    def __init__(self):
        super().__init__("Bulk Up", type=Type.FIGHTING, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and Defense.
        """
        pass
