from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SupersonicSkystrike(Move):
    def __init__(self):
        super().__init__("Supersonic Skystrike", type=TypeFactory.create_type(Types.FLYING), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Flying type Z-Move.
        """
        pass
