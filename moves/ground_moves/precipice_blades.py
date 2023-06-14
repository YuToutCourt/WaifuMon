from ..move import Move
from waifu_types.type import Type

class PrecipiceBlades(Move):
    def __init__(self):
        super().__init__("Precipice Blades", type=Type.GROUND, power=120, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
