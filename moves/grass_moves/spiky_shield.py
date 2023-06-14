from ..move import Move
from waifu_types.type import Type

class SpikyShield(Move):
    def __init__(self):
        super().__init__("Spiky Shield", type=Type.GRASS, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user and inflicts damage on contact.
        """
        pass
