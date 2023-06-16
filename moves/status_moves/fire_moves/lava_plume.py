from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class LavaPlume(Move):
    def __init__(self):
        super().__init__("Lava Plume", type=TypeFactory.create_type(Types.FIRE), power=80, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
