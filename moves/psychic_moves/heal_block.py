from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HealBlock(Move):
    def __init__(self):
        super().__init__("Heal Block", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents the opponent from restoring HP for 5 turns.
        """
        pass
