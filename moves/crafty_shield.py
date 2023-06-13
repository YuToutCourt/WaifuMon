from .move import Move
from waifu_types.type import Type

class CraftyShield(Move):
    def __init__(self):
        super().__init__("Crafty Shield", type=Type.FAIRY, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the Pokémon from status moves.
        """
        pass
