from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BreakneckBlitz(Move):
    def __init__(self):
        super().__init__(
            "Breakneck Blitz",
            type=TypeFactory.create_type(Types.NORMAL),
            power=190,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Normal type Z-Move.
        """
        pass
