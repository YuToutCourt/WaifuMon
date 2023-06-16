from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Gust(Move):
    def __init__(self):
        super().__init__(
            "Gust",
            type=TypeFactory.create_type(Types.FLYING),
            power=40,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits Pokemon using Fly/Bounce/Sky Drop with double power.
        """
        pass
