from ..move import Move
from waifu_types.type import Type

class MagneticFlux(Move):
    def __init__(self):
        super().__init__("Magnetic Flux", type=Type.ELECTRIC, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Defense and Sp. Defense of Plus/Minus Pokémon.
        """
        pass
