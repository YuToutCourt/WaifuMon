from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Bite(Move):
    def __init__(self):
        super().__init__("Bite", type=TypeFactory.create_type(Types.DARK), power=60, accuracy=100, pp=25, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
