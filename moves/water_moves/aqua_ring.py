from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AquaRing(Move):
    def __init__(self):
        super().__init__("Aqua Ring", type=TypeFactory.create_type(Types.WATER), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Restores a little HP each turn.
        """
        pass
