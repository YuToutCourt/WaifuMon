from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Eternabeam(Move):
    def __init__(self):
        super().__init__("Eternabeam", type=TypeFactory.create_type(Types.DRAGON), power=160, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User can't move on the next turn.
        """
        pass
