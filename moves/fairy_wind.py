from .move import Move
from waifu_types.type import Type

class FairyWind(Move):
    def __init__(self):
        super().__init__("Fairy Wind", type=Type.FAIRY, power=40, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
