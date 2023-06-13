from .move import Move
from waifu_types.type import Type

class Constrict(Move):
    def __init__(self):
        super().__init__("Constrict", type=Type.NORMAL, power=10, accuracy=100, pp=35, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Speed by one stage.
        """
        pass
