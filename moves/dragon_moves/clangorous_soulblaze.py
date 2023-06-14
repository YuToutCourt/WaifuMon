from ..move import Move
from waifu_types.type import Type

class ClangorousSoulblaze(Move):
    def __init__(self):
        super().__init__("Clangorous Soulblaze", type=Type.DRAGON, power=185, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Kommo-o exclusive Z-Move.
        """
        pass
