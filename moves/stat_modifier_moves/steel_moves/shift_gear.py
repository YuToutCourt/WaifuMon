from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ShiftGear(Move):
    def __init__(self):
        super().__init__(
            "Shift Gear",
            type=TypeFactory.create_type(Types.STEEL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack and sharply raises Speed.
        """
        pass
