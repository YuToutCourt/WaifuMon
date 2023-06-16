from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Autotomize(Move):
    def __init__(self):
        super().__init__("Autotomize", type=TypeFactory.create_type(Types.STEEL), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Reduces weight and sharply raises Speed.
        """
        pass
