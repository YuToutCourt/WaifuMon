from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Octolock(Move):
    def __init__(self):
        super().__init__(
            "Octolock",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Defense and Special Defense every turn, and they cannot flee or switch out.
        """
        pass
