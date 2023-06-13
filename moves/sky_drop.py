from .move import Move
from waifu_types.type import Type

class SkyDrop(Move):
    def __init__(self):
        super().__init__("Sky Drop", type=Type.FLYING, power=60, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Takes opponent into the air on first turn, drops them on second turn.
        """
        pass
