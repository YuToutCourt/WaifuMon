from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Swagger(Move):
    def __init__(self):
        super().__init__("Swagger", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=85, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent, but sharply raises its Attack.
        """
        pass
