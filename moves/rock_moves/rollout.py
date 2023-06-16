from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Rollout(Move):
    def __init__(self):
        super().__init__(
            "Rollout",
            type=TypeFactory.create_type(Types.ROCK),
            power=30,
            accuracy=90,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Doubles in power each turn for 5 turns.
        """
        pass
