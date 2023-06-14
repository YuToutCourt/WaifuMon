from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SavageSpin-Out(Move):
    def __init__(self):
        super().__init__("Savage Spin-Out", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Bug type Z-Move.
        """
        pass
