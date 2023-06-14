from ..move import Move
from waifu_types.type import Type

class MagicPowder(Move):
    def __init__(self):
        super().__init__("Magic Powder", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes target's type to Psychic.
        """
        pass
