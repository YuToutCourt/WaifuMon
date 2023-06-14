from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FlipTurn(Move):
    def __init__(self):
        super().__init__("Flip Turn", type=TypeFactory.create_type(Types.WATER), power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        After making its attack, the user rushes back to switch places with a party Pokémon in waiting.
        """
        pass
