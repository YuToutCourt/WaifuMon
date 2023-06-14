from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Synchronoise(Move):
    def __init__(self):
        super().__init__("Synchronoise", type=TypeFactory.create_type(Types.PSYCHIC), power=120, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits any Pokémon that shares a type with the user.
        """
        pass
