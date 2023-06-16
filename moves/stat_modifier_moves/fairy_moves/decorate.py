from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Decorate(Move):
    def __init__(self):
        super().__init__(
            "Decorate",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Sharply raises target's Attack and Special Attack.
        """
        pass
