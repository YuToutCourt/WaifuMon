from ..move import Move
from waifu_types.type import Type

class G-MaxRapidFlow(Move):
    def __init__(self):
        super().__init__("G-Max Rapid Flow", type=Type.WATER, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Urshifu Rapid-Strike Style-exclusive G-Max Move. Strikes through Max Guard and Protect.
        """
        pass
