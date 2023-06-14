from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ShedTail(Move):
    def __init__(self):
        super().__init__("Shed Tail", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Creates a substitute, then swaps places with a party Pokémon in waiting.
        """
        pass
