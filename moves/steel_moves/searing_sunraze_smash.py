from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SearingSunrazeSmash(Move):
    def __init__(self):
        super().__init__(
            "Searing Sunraze Smash",
            type=TypeFactory.create_type(Types.STEEL),
            power=200,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Solgaleo-exclusive Z-Move.
        """
        pass
