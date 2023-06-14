from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Incinerate(Move):
    def __init__(self):
        super().__init__("Incinerate", type=TypeFactory.create_type(Types.FIRE), power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Destroys the target's held berry.
        """
        pass
