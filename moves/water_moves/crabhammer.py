from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Crabhammer(Move):
    def __init__(self):
        super().__init__("Crabhammer", type=TypeFactory.create_type(Types.WATER), power=100, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
