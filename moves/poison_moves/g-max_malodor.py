from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxMalodor(Move):
    def __init__(self):
        super().__init__("G-Max Malodor", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Garbodor-exclusive G-Max Move. Poisons opponents.
        """
        pass
