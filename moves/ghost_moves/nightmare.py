from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Nightmare(Move):
    def __init__(self):
        super().__init__("Nightmare", type=TypeFactory.create_type(Types.GHOST), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The sleeping opponent loses 25% of its max HP each turn.
        """
        pass
