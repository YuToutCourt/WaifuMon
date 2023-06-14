from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SandAttack(Move):
    def __init__(self):
        super().__init__("Sand Attack", type=TypeFactory.create_type(Types.GROUND), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass
