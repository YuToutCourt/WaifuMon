from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxCannonade(Move):
    def __init__(self):
        super().__init__("G-Max Cannonade", type=TypeFactory.create_type(Types.WATER), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Blastoise-exclusive G-Max Move. Damages non-Water types for 4 turns.
        """
        pass
