from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AromaticMist(Move):
    def __init__(self):
        super().__init__("Aromatic Mist", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Special Defense of an ally.
        """
        pass
