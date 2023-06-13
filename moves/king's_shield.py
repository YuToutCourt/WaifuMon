from .move import Move
from waifu_types.type import Type

class King'sShield(Move):
    def __init__(self):
        super().__init__("King's Shield", type=Type.STEEL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the user and lowers opponent's Attack on contact.
        """
        pass
