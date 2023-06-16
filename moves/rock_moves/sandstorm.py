from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Sandstorm(Move):
    def __init__(self):
        super().__init__(
            "Sandstorm",
            type=TypeFactory.create_type(Types.ROCK),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Creates a sandstorm for 5 turns.
        """
        pass
