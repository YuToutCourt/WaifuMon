from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ContinentalCrush(Move):
    def __init__(self):
        super().__init__(
            "Continental Crush",
            type=TypeFactory.create_type(Types.ROCK),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Rock type Z-Move.
        """
        pass
