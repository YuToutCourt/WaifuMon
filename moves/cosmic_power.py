from .move import Move
from waifu_types.type import Type

class CosmicPower(Move):
    def __init__(self):
        super().__init__("Cosmic Power", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Raises user's Defense and Special Defense.
        """
        pass
