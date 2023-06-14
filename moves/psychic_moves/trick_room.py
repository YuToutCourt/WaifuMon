from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TrickRoom(Move):
    def __init__(self):
        super().__init__("Trick Room", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Slower Pokémon move first in the turn for 5 turns.
        """
        pass
