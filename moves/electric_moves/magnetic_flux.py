from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MagneticFlux(Move):
    def __init__(self):
        super().__init__("Magnetic Flux", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Defense and Sp. Defense of Plus/Minus Pokémon.
        """
        pass
