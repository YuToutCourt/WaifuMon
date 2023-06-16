from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PowerSwap(Move):
    def __init__(self):
        super().__init__(
            "Power Swap",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User and opponent swap Attack and Special Attack.
        """
        pass
