from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxBefuddle(Move):
    def __init__(self):
        super().__init__("G-Max Befuddle", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Butterfree-exclusive G-Max Move. Poisons, paralyzes, or puts opponent to sleep.
        """
        pass
