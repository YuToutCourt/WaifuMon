from .move import Move
from waifu_types.type import Type

class WorrySeed(Move):
    def __init__(self):
        super().__init__("Worry Seed", type=Type.GRASS, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Changes the opponent's Ability to Insomnia.
        """
        pass
