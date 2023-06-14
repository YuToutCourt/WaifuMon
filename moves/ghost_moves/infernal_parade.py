from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class InfernalParade(Move):
    def __init__(self):
        super().__init__("Infernal Parade", type=TypeFactory.create_type(Types.GHOST), power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target has a status condition.
        """
        pass
