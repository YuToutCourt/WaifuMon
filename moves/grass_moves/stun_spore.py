from ..move import Move
from waifu_types.type import Type

class StunSpore(Move):
    def __init__(self):
        super().__init__("Stun Spore", type=Type.GRASS, power=0, accuracy=75, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
