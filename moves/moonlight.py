from .move import Move
from waifu_types.type import Type

class Moonlight(Move):
    def __init__(self):
        super().__init__("Moonlight", type=Type.FAIRY, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User recovers HP. Amount varies with the weather.
        """
        pass
