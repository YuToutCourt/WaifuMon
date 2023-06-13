from .move import Move
from waifu_types.type import Type

class SilkTrap(Move):
    def __init__(self):
        super().__init__("Silk Trap", type=Type.BUG, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the user and lowers opponent's Speed on contact.
        """
        pass
