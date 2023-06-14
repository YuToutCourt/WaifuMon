from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Poltergeist(Move):
    def __init__(self):
        super().__init__("Poltergeist", type=TypeFactory.create_type(Types.GHOST), power=110, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Fails if the target doesn’t have an item.
        """
        pass
