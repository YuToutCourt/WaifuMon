from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FreezeDry(Move):
    def __init__(self):
        super().__init__(
            "Freeze-Dry",
            type=TypeFactory.create_type(Types.ICE),
            power=70,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May freeze opponent. Super-effective against Water types.
        """
        pass
