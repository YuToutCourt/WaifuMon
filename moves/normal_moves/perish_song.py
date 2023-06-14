from ..move import Move
from waifu_types.type import Type

class PerishSong(Move):
    def __init__(self):
        super().__init__("Perish Song", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Any Pokémon in play when this attack is used faints in 3 turns.
        """
        pass
