from ..move import Move
from waifu_types.type import Type

class HydroPump(Move):
    def __init__(self):
        super().__init__("Hydro Pump", type=Type.WATER, power=110, accuracy=80, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
