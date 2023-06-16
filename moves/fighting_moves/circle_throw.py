from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CircleThrow(Move):
    def __init__(self):
        super().__init__(
            "Circle Throw",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=60,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        In battles, the opponent switches. In the wild, the Pokemon runs.
        """
        pass
