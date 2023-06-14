from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ThunderFang(Move):
    def __init__(self):
        super().__init__("Thunder Fang", type=TypeFactory.create_type(Types.ELECTRIC), power=65, accuracy=95, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May cause flinching and/or paralyze opponent.
        """
        pass
