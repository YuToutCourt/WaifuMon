from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PainSplit(Move):
    def __init__(self):
        super().__init__("Pain Split", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        The user's and opponent's HP becomes the average of both.
        """
        pass
