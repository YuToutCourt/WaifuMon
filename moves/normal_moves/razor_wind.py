from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RazorWind(Move):
    def __init__(self):
        super().__init__(
            "Razor Wind",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Charges on first turn, attacks on second. High critical hit ratio.
        """
        pass
