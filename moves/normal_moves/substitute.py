from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Substitute(Move):
    def __init__(self):
        super().__init__("Substitute", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Uses HP to creates a decoy that takes hits.
        """
        pass
