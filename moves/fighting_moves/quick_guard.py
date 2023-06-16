from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class QuickGuard(Move):
    def __init__(self):
        super().__init__(
            "Quick Guard",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Protects the user's team from high-priority moves.
        """
        pass
