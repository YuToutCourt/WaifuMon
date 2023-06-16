from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Haze(Move):
    def __init__(self):
        super().__init__(
            "Haze",
            type=TypeFactory.create_type(Types.ICE),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Resets all stat changes.
        """
        pass
