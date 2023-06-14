from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Supersonic(Move):
    def __init__(self):
        super().__init__("Supersonic", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=55, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
