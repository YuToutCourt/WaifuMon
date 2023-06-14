from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class StoneAxe(Move):
    def __init__(self):
        super().__init__("Stone Axe", type=TypeFactory.create_type(Types.ROCK), power=65, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. Damages target with splinters each turn.
        """
        pass
