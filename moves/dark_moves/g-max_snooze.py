from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxSnooze(Move):
    def __init__(self):
        super().__init__("G-Max Snooze", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Grimmsnarl-exclusive G-Max Move. Makes opponents drowsy.
        """
        pass
