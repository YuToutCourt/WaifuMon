from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Lick(Move):
    def __init__(self):
        super().__init__(
            "Lick",
            type=TypeFactory.create_type(Types.GHOST),
            power=30,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
