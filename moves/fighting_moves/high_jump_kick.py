from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HighJumpKick(Move):
    def __init__(self):
        super().__init__(
            "High Jump Kick",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=130,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        If it misses, the user loses half their HP.
        """
        pass
