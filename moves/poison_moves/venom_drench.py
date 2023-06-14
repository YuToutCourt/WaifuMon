from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class VenomDrench(Move):
    def __init__(self):
        super().__init__("Venom Drench", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers poisoned opponent's Special Attack and Speed.
        """
        pass
