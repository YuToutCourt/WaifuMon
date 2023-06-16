from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Coaching(Move):
    def __init__(self):
        super().__init__(
            "Coaching",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Boosts Attack and Defense of a teammate.
        """
        pass
