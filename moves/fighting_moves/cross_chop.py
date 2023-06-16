from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CrossChop(Move):
    def __init__(self):
        super().__init__(
            "Cross Chop",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=100,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
