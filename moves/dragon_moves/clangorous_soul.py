from ..move import Move
from waifu_types.type import Type

class ClangorousSoul(Move):
    def __init__(self):
        super().__init__("Clangorous Soul", type=Type.DRAGON, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises all user's stats but loses HP.
        """
        pass
