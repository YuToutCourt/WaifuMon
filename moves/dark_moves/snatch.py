from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Snatch(Move):
    def __init__(self):
        super().__init__(
            "Snatch",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Steals the effects of the opponent's next move.
        """
        pass
