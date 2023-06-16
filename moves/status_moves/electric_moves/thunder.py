from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Thunder(Move):
    def __init__(self):
        super().__init__(
            "Thunder",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=110,
            accuracy=70,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
