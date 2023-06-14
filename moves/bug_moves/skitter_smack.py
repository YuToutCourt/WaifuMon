from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SkitterSmack(Move):
    def __init__(self):
        super().__init__("Skitter Smack", type=TypeFactory.create_type(Types.BUG), power=70, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Sp. Attack.
        """
        pass
