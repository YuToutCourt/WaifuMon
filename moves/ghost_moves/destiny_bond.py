from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DestinyBond(Move):
    def __init__(self):
        super().__init__("Destiny Bond", type=TypeFactory.create_type(Types.GHOST), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        If the user faints, the opponent also faints.
        """
        pass
