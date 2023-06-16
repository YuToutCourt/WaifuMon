from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FireBlast(Move):
    def __init__(self):
        super().__init__("Fire Blast", type=TypeFactory.create_type(Types.FIRE), power=110, accuracy=85, pp=5, priority=0, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
