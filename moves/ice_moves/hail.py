from ..move import Move
from waifu_types.type import Type

class Hail(Move):
    def __init__(self):
        super().__init__("Hail", type=Type.ICE, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Non-Ice types are damaged for 5 turns.
        """
        pass
