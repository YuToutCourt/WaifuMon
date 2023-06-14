from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SmackDown(Move):
    def __init__(self):
        super().__init__("Smack Down", type=TypeFactory.create_type(Types.ROCK), power=50, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Makes Flying-type Pokémon vulnerable to Ground moves.
        """
        pass
