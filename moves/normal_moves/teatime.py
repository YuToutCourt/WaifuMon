from ..move import Move
from waifu_types.type import Type

class Teatime(Move):
    def __init__(self):
        super().__init__("Teatime", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Forces all Pokémon on the field to eat their berries.
        """
        pass
