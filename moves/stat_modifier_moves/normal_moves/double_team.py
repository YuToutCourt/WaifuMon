from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DoubleTeam(Move):
    def __init__(self):
        super().__init__(
            "Double Team",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Evasiveness.
        """
        pass
