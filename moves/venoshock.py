from .move import Move
from waifu_types.type import Type

class Venoshock(Move):
    def __init__(self):
        super().__init__("Venoshock", type=Type.POISON, power=65, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target is poisoned.
        """
        pass
