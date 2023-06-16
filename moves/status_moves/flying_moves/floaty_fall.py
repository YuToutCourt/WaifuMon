from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FloatyFall(Move):
    def __init__(self):
        super().__init__(
            "Floaty Fall",
            type=TypeFactory.create_type(Types.FLYING),
            power=90,
            accuracy=95,
            pp=15,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May cause flinching.
        """
        pass
