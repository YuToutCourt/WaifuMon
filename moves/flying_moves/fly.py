from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Fly(Move):
    def __init__(self):
        super().__init__("Fly", type=TypeFactory.create_type(Types.FLYING), power=90, accuracy=95, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Flies up on first turn, attacks on second turn.
        """
        pass
