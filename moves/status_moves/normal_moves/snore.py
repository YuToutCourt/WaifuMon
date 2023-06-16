from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Snore(Move):
    def __init__(self):
        super().__init__("Snore", type=TypeFactory.create_type(Types.NORMAL), power=50, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        Can only be used if asleep. May cause flinching.
        """
        pass
