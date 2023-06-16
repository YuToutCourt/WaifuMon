from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WonderRoom(Move):
    def __init__(self):
        super().__init__(
            "Wonder Room",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Swaps every Pokemon's Defense and Special Defense for 5 turns.
        """
        pass
