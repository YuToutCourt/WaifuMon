from .move import Move
from waifu_types.type import Type

class DrillPeck(Move):
    def __init__(self):
        super().__init__("Drill Peck", type=Type.FLYING, power=80, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
