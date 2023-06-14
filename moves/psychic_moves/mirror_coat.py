from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MirrorCoat(Move):
    def __init__(self):
        super().__init__("Mirror Coat", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        When hit by a Special Attack, user strikes back with 2x power.
        """
        pass
