from ..move import Move
from waifu_types.type import Type

class ThousandArrows(Move):
    def __init__(self):
        super().__init__("Thousand Arrows", type=Type.GROUND, power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Makes Flying-type Pokémon vulnerable to Ground moves.
        """
        pass
