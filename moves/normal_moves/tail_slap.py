from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TailSlap(Move):
    def __init__(self):
        super().__init__(
            "Tail Slap",
            type=TypeFactory.create_type(Types.NORMAL),
            power=25,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
