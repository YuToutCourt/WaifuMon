from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Comeuppance(Move):
    def __init__(self):
        super().__init__(
            "Comeuppance",
            type=TypeFactory.create_type(Types.DARK),
            power=1,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Deals more damage to the opponent that last inflicted damage on it.
        """
        pass
