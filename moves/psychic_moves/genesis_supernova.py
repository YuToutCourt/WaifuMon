from ..move import Move
from waifu_types.type import Type

class GenesisSupernova(Move):
    def __init__(self):
        super().__init__("Genesis Supernova", type=Type.PSYCHIC, power=185, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Mew-exclusive Z-Move.
        """
        pass
