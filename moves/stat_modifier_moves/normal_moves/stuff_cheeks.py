from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class StuffCheeks(Move):
    def __init__(self):
        super().__init__("Stuff Cheeks", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user eats its held Berry, then sharply raises its Defense stat.
        """
        pass
