from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BarbBarrage(Move):
    def __init__(self):
        super().__init__("Barb Barrage", type=TypeFactory.create_type(Types.POISON), power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target has a status condition.
        """
        pass
