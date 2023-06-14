from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Guillotine(Move):
    def __init__(self):
        super().__init__("Guillotine", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=30, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        One-Hit-KO, if it hits.
        """
        pass
