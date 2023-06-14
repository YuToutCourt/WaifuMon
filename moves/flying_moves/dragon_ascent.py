from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DragonAscent(Move):
    def __init__(self):
        super().__init__("Dragon Ascent", type=TypeFactory.create_type(Types.FLYING), power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense and Special Defense.
        """
        pass
