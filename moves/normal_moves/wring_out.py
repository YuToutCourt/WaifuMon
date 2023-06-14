from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class WringOut(Move):
    def __init__(self):
        super().__init__("Wring Out", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The higher the opponent's HP, the higher the damage.
        """
        pass
