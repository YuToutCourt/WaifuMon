from ..move import Move
from waifu_types.type import Type

class Shelter(Move):
    def __init__(self):
        super().__init__("Shelter", type=Type.STEEL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Defense and Evasion.
        """
        pass
