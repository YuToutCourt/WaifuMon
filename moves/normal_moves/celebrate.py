from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Celebrate(Move):
    def __init__(self):
        super().__init__("Celebrate", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        The Pokémon congratulates you on your special day. No battle effect.
        """
        pass
