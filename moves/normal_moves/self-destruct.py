from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Self-Destruct(Move):
    def __init__(self):
        super().__init__("Self-Destruct", type=TypeFactory.create_type(Types.NORMAL), power=200, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User faints.
        """
        pass
