from .move import Move
from waifu_types.type import Type

class HealingWish(Move):
    def __init__(self):
        super().__init__("Healing Wish", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user faints and the next Pokémon released is fully healed.
        """
        pass
