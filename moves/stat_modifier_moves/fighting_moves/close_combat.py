from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CloseCombat(Move):
    def __init__(self):
        super().__init__(
            "Close Combat",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers user's Defense and Special Defense.
        """
        pass
