from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpacialRend(Move):
    def __init__(self):
        super().__init__("Spacial Rend", type=TypeFactory.create_type(Types.DRAGON), power=100, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
