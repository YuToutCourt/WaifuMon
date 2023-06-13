from .move import Move
from waifu_types.type import Type

class BranchPoke(Move):
    def __init__(self):
        super().__init__("Branch Poke", type=Type.GRASS, power=40, accuracy=100, pp=40, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
