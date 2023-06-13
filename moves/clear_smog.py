from .move import Move
from waifu_types.type import Type

class ClearSmog(Move):
    def __init__(self):
        super().__init__("Clear Smog", type=Type.POISON, power=50, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Removes all of the target's stat changes.
        """
        pass
