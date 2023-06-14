from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DragonRush(Move):
    def __init__(self):
        super().__init__("Dragon Rush", type=TypeFactory.create_type(Types.DRAGON), power=100, accuracy=75, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass
