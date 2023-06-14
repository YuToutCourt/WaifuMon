from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class LuckyChant(Move):
    def __init__(self):
        super().__init__("Lucky Chant", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot land critical hits for 5 turns.
        """
        pass
