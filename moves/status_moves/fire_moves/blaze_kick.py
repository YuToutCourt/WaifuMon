from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BlazeKick(Move):
    def __init__(self):
        super().__init__("Blaze Kick", type=TypeFactory.create_type(Types.FIRE), power=85, accuracy=90, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        High critical hit ratio. May burn opponent.
        """
        pass
