from ..move import Move
from waifu_types.type import Type

class BeatUp(Move):
    def __init__(self):
        super().__init__("Beat Up", type=Type.DARK, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Each Pokémon in user's party attacks.
        """
        pass
