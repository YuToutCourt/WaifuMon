from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Assist(Move):
    def __init__(self):
        super().__init__("Assist", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User performs a move known by its allies at random.
        """
        pass
