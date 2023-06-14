from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Thunderbolt(Move):
    def __init__(self):
        super().__init__("Thunderbolt", type=TypeFactory.create_type(Types.ELECTRIC), power=90, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
