from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DynamaxCannon(Move):
    def __init__(self):
        super().__init__("Dynamax Cannon", type=TypeFactory.create_type(Types.DRAGON), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Damage doubles if opponent is Dynamaxed.
        """
        pass
