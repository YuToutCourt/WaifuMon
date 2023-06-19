from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TwinkleTackle(Move):
    def __init__(self):
        super().__init__(
            "Twinkle Tackle",
            type=TypeFactory.create_type(Types.FAIRY),
            power=120,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Fairy type Z-Move.
        """
        pass
