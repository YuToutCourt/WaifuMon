from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LastRespects(Move):
    def __init__(self):
        super().__init__(
            "Last Respects",
            type=TypeFactory.create_type(Types.GHOST),
            power=50,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Damages increases the more party Pokemon have been defeated.
        """
        pass
