from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DireClaw(Move):
    def __init__(self):
        super().__init__("Dire Claw", type=TypeFactory.create_type(Types.POISON), power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. May poison, paralyze or make the opponent drowsy.
        """
        pass
