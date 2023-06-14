from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Teleport(Move):
    def __init__(self):
        super().__init__("Teleport", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Allows user to flee wild battles; also warps player to last PokéCenter.
        """
        pass
