from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WillOWisp(Move):
    def __init__(self):
        super().__init__(
            "Will-O-Wisp",
            type=TypeFactory.create_type(Types.FIRE),
            power=0,
            accuracy=85,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Burns opponent.
        """
        pass
