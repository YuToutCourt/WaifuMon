from .move import Move
from waifu_types.type import Type

class InfernalParade(Move):
    def __init__(self):
        super().__init__("Infernal Parade", type=Type.GHOST, power=60, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target has a status condition.
        """
        pass
