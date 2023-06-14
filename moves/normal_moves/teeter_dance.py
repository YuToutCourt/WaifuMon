from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TeeterDance(Move):
    def __init__(self):
        super().__init__("Teeter Dance", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses all Pokémon.
        """
        pass
