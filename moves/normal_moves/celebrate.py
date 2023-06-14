from ..move import Move
from waifu_types.type import Type

class Celebrate(Move):
    def __init__(self):
        super().__init__("Celebrate", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        The Pokémon congratulates you on your special day. No battle effect.
        """
        pass
