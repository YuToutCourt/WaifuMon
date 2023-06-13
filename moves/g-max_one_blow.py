from .move import Move
from waifu_types.type import Type

class G-MaxOneBlow(Move):
    def __init__(self):
        super().__init__("G-Max One Blow", type=Type.DARK, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Urshifu Single-Strike Style-exclusive G-Max Move. Strikes through Max Guard and Protect.
        """
        pass
