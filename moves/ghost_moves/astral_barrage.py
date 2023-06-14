from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AstralBarrage(Move):
    def __init__(self):
        super().__init__("Astral Barrage", type=TypeFactory.create_type(Types.GHOST), power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The user attacks by sending a frightful amount of small ghosts at opposing Pokémon.
        """
        pass
