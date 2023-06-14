from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxStunShock(Move):
    def __init__(self):
        super().__init__("G-Max Stun Shock", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Toxtricity-exclusive G-Max Move. Poisons or paralyzes opponents.
        """
        pass
