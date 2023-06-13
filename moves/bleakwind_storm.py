from .move import Move
from waifu_types.type import Type

class BleakwindStorm(Move):
    def __init__(self):
        super().__init__("Bleakwind Storm", type=Type.FLYING, power=100, accuracy=80, pp=10, proba_effect=100)

    def effect(self):
        """
        May cause frostbite.
        """
        pass
