from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PoisonSting(Move):
    def __init__(self):
        super().__init__(
            "Poison Sting",
            type=TypeFactory.create_type(Types.POISON),
            power=15,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May poison the opponent.
        """
        pass
