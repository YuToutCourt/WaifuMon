from .move import Move
from waifu_types.type import Type

class Stomp(Move):
    def __init__(self):
        super().__init__("Stomp", type=Type.NORMAL, power=65, accuracy=100, pp=20, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
