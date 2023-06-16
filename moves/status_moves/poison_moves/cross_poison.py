from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CrossPoison(Move):
    def __init__(self):
        super().__init__(
            "Cross Poison",
            type=TypeFactory.create_type(Types.POISON),
            power=70,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        High critical hit ratio. May poison opponent.
        """
        pass
