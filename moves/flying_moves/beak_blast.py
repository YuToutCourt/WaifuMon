from ..move import Move
from waifu_types.type import Type

class BeakBlast(Move):
    def __init__(self):
        super().__init__("Beak Blast", type=Type.FLYING, power=100, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The user first heats up its beak, and then it attacks the target. Making direct contact with the Pokémon while it's heating up its beak results in a burn.
        """
        pass
