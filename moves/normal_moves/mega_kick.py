from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MegaKick(Move):
    def __init__(self):
        super().__init__(
            "Mega Kick",
            type=TypeFactory.create_type(Types.NORMAL),
            power=120,
            accuracy=75,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass
