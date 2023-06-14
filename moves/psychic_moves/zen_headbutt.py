from ..move import Move
from waifu_types.type import Type

class ZenHeadbutt(Move):
    def __init__(self):
        super().__init__("Zen Headbutt", type=Type.PSYCHIC, power=80, accuracy=90, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass
