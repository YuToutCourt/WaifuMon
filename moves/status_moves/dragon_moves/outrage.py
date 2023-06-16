from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Outrage(Move):
    def __init__(self):
        super().__init__(
            "Outrage",
            type=TypeFactory.create_type(Types.DRAGON),
            power=120,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User attacks for 2-3 turns but then becomes confused.
        """
        pass