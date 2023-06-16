from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ForcePalm(Move):
    def __init__(self):
        super().__init__("Force Palm", type=TypeFactory.create_type(Types.FIGHTING), power=60, accuracy=100, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
