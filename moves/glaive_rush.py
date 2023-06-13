from .move import Move
from waifu_types.type import Type

class GlaiveRush(Move):
    def __init__(self):
        super().__init__("Glaive Rush", type=Type.DRAGON, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Attacks from opposing Pokémon during the next turn cannot miss and will inflict double damage.
        """
        pass
