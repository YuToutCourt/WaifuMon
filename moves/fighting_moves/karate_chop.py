from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class KarateChop(Move):
    def __init__(self):
        super().__init__(
            "Karate Chop",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
