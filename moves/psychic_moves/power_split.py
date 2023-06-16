from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PowerSplit(Move):
    def __init__(self):
        super().__init__(
            "Power Split",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Averages Attack and Special Attack with the target.
        """
        pass
