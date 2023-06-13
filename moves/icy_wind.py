from .move import Move
from waifu_types.type import Type

class IcyWind(Move):
    def __init__(self):
        super().__init__("Icy Wind", type=Type.ICE, power=55, accuracy=95, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
