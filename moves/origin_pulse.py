from .move import Move
from waifu_types.type import Type

class OriginPulse(Move):
    def __init__(self):
        super().__init__("Origin Pulse", type=Type.WATER, power=110, accuracy=85, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
