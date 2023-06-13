from .move import Move
from waifu_types.type import Type

class TrickRoom(Move):
    def __init__(self):
        super().__init__("Trick Room", type=Type.PSYCHIC, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Slower Pokémon move first in the turn for 5 turns.
        """
        pass
