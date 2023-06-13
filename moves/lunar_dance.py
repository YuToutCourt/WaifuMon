from .move import Move
from waifu_types.type import Type

class LunarDance(Move):
    def __init__(self):
        super().__init__("Lunar Dance", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user faints but the next Pokémon released is fully healed.
        """
        pass
