from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FoulPlay(Move):
    def __init__(self):
        super().__init__(
            "Foul Play",
            type=TypeFactory.create_type(Types.DARK),
            power=95,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Uses the opponent's Attack stat.
        """
        pass
