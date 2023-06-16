from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Bubble(Move):
    def __init__(self):
        super().__init__(
            "Bubble",
            type=TypeFactory.create_type(Types.WATER),
            power=40,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May lower opponent's Speed.
        """
        pass
