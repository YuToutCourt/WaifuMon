from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Thief(Move):
    def __init__(self):
        super().__init__(
            "Thief",
            type=TypeFactory.create_type(Types.DARK),
            power=60,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Also steals opponent's held item.
        """
        pass
