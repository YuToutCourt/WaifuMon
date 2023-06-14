from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Flatter(Move):
    def __init__(self):
        super().__init__("Flatter", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent, but raises its Special Attack.
        """
        pass
