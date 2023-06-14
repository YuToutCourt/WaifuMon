from ..move import Move
from waifu_types.type import Type

class RevivalBlessing(Move):
    def __init__(self):
        super().__init__("Revival Blessing", type=Type.NORMAL, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Revives a fainted party Pokémon to half HP.
        """
        pass
