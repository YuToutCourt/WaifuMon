from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Fissure(Move):
    def __init__(self):
        super().__init__("Fissure", type=TypeFactory.create_type(Types.GROUND), power=0, accuracy=30, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        One-Hit-KO, if it hits.
        """
        pass
