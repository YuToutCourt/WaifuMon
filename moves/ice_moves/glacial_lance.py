from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GlacialLance(Move):
    def __init__(self):
        super().__init__("Glacial Lance", type=TypeFactory.create_type(Types.ICE), power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The user attacks by hurling a blizzard-cloaked icicle lance at opposing Pokémon.
        """
        pass
