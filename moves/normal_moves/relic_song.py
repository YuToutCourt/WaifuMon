from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RelicSong(Move):
    def __init__(self):
        super().__init__(
            "Relic Song",
            type=TypeFactory.create_type(Types.NORMAL),
            power=75,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May put the target to sleep.
        """
        pass
