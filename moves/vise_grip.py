from .move import Move
from waifu_types.type import Type

class ViseGrip(Move):
    def __init__(self):
        super().__init__("Vise Grip", type=Type.NORMAL, power=55, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
