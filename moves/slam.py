from .move import Move
from waifu_types.type import Type

class Slam(Move):
    def __init__(self):
        super().__init__("Slam", type=Type.NORMAL, power=80, accuracy=75, pp=20, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
