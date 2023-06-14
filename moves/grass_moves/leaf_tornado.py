from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class LeafTornado(Move):
    def __init__(self):
        super().__init__("Leaf Tornado", type=TypeFactory.create_type(Types.GRASS), power=65, accuracy=90, pp=10, priority=0, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
