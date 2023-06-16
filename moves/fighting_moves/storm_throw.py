from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class StormThrow(Move):
    def __init__(self):
        super().__init__(
            "Storm Throw",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=60,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass
