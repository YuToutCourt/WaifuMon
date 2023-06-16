from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ClangingScales(Move):
    def __init__(self):
        super().__init__(
            "Clanging Scales",
            type=TypeFactory.create_type(Types.DRAGON),
            power=110,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers user's Defense.
        """
        pass
