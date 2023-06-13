from .move import Move
from waifu_types.type import Type

class Land'sWrath(Move):
    def __init__(self):
        super().__init__("Land's Wrath", type=Type.GROUND, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
