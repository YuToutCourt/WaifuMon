from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TailGlow(Move):
    def __init__(self):
        super().__init__("Tail Glow", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Drastically raises user's Special Attack.
        """
        pass
