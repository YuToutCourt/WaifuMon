from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class VoltTackle(Move):
    def __init__(self):
        super().__init__("Volt Tackle", type=TypeFactory.create_type(Types.ELECTRIC), power=120, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        User receives recoil damage. May paralyze opponent.
        """
        pass
