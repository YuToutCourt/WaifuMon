from .move import Move
from waifu_types.type import Type

class VictoryDance(Move):
    def __init__(self):
        super().__init__("Victory Dance", type=Type.FIGHTING, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises Attack and Defense.
        """
        pass
