from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpiritShackle(Move):
    def __init__(self):
        super().__init__("Spirit Shackle", type=TypeFactory.create_type(Types.GHOST), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents the opponent from switching out.
        """
        pass
