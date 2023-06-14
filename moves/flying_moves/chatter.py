from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Chatter(Move):
    def __init__(self):
        super().__init__("Chatter", type=TypeFactory.create_type(Types.FLYING), power=65, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
