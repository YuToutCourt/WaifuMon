from ..move import Move
from waifu_types.type import Type

class SteamEruption(Move):
    def __init__(self):
        super().__init__("Steam Eruption", type=Type.WATER, power=110, accuracy=95, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
