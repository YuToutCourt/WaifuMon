from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxDepletion(Move):
    def __init__(self):
        super().__init__("G-Max Depletion", type=TypeFactory.create_type(Types.DRAGON), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Duraludon-exclusive G-Max Move. Reduces opponent's PP.
        """
        pass
