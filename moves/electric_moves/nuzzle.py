from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Nuzzle(Move):
    def __init__(self):
        super().__init__(
            "Nuzzle",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=20,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
