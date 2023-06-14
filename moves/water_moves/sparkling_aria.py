from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SparklingAria(Move):
    def __init__(self):
        super().__init__("Sparkling Aria", type=TypeFactory.create_type(Types.WATER), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Heals the burns of its target.
        """
        pass
