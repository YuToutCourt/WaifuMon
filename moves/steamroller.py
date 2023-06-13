from .move import Move
from waifu_types.type import Type

class Steamroller(Move):
    def __init__(self):
        super().__init__("Steamroller", type=Type.BUG, power=65, accuracy=100, pp=20, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
