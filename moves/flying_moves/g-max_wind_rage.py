from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxWindRage(Move):
    def __init__(self):
        super().__init__("G-Max Wind Rage", type=TypeFactory.create_type(Types.FLYING), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Corviknight-exclusive G-Max Move. Removes battlefield hazards.
        """
        pass
