from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Hex(Move):
    def __init__(self):
        super().__init__("Hex", type=TypeFactory.create_type(Types.GHOST), power=65, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts more damage if the target has a status condition.
        """
        pass
