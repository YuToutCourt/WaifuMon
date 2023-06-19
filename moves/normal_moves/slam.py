from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Slam(Move):
    def __init__(self):
        super().__init__(
            "Slam",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=75,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass
