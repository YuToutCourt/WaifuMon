from ..move import Move
from waifu_types.type import Type

class BatonPass(Move):
    def __init__(self):
        super().__init__("Baton Pass", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        User switches out and gives stat changes to the incoming Pokémon.
        """
        pass
