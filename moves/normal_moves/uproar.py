from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Uproar(Move):
    def __init__(self):
        super().__init__("Uproar", type=TypeFactory.create_type(Types.NORMAL), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User attacks for 3 turns and prevents sleep.
        """
        pass
