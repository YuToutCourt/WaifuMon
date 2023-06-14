from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MoongeistBeam(Move):
    def __init__(self):
        super().__init__("Moongeist Beam", type=TypeFactory.create_type(Types.GHOST), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores the target's ability.
        """
        pass
