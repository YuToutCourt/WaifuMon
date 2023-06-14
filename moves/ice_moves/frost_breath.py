from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FrostBreath(Move):
    def __init__(self):
        super().__init__("Frost Breath", type=TypeFactory.create_type(Types.ICE), power=60, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass
