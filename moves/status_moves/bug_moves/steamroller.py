from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Steamroller(Move):
    def __init__(self):
        super().__init__("Steamroller", type=TypeFactory.create_type(Types.BUG), power=65, accuracy=100, pp=20, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
