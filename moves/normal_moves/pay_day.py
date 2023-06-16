from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PayDay(Move):
    def __init__(self):
        super().__init__(
            "Pay Day",
            type=TypeFactory.create_type(Types.NORMAL),
            power=40,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Money is earned after the battle.
        """
        pass
