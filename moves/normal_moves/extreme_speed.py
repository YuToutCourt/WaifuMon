from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ExtremeSpeed(Move):
    def __init__(self):
        super().__init__(
            "Extreme Speed",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=100,
            pp=5,
            priority=1,
            proba_effect=100,
        )

    def effect(self):
        """
        User attacks first.
        """
        pass
