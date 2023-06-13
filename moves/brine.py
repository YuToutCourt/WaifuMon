from .move import Move
from waifu_types.type import Type

class Brine(Move):
    def __init__(self):
        super().__init__("Brine", type=Type.WATER, power=65, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Power doubles if opponent's HP is less than 50%.
        """
        pass
