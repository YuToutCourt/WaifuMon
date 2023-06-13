from .move import Move
from waifu_types.type import Type

class Snowscape(Move):
    def __init__(self):
        super().__init__("Snowscape", type=Type.ICE, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises Defense of Ice types for 5 turns.
        """
        pass
