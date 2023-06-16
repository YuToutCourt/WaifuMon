from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DiamondStorm(Move):
    def __init__(self):
        super().__init__(
            "Diamond Storm",
            type=TypeFactory.create_type(Types.ROCK),
            power=100,
            accuracy=95,
            pp=5,
            priority=0,
            proba_effect=50,
        )

    def effect(self):
        """
        May sharply raise user's Defense.
        """
        pass
