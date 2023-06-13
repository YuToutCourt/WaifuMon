from .move import Move
from waifu_types.type import Type

class IceFang(Move):
    def __init__(self):
        super().__init__("Ice Fang", type=Type.ICE, power=65, accuracy=95, pp=15, proba_effect=10)

    def effect(self):
        """
        May cause flinching and/or freeze opponent.
        """
        pass
