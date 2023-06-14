from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Pluck(Move):
    def __init__(self):
        super().__init__("Pluck", type=TypeFactory.create_type(Types.FLYING), power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        If the opponent is holding a berry, its effect is stolen by user.
        """
        pass
