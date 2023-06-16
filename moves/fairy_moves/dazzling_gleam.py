from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DazzlingGleam(Move):
    def __init__(self):
        super().__init__(
            "Dazzling Gleam",
            type=TypeFactory.create_type(Types.FAIRY),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
