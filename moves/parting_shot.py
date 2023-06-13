from .move import Move
from waifu_types.type import Type

class PartingShot(Move):
    def __init__(self):
        super().__init__("Parting Shot", type=Type.DARK, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Attack and Special Attack then switches out. 
        """
        pass
