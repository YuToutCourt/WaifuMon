from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SpinOut(Move):
    def __init__(self):
        super().__init__(
            "Spin Out",
            type=TypeFactory.create_type(Types.STEEL),
            power=100,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Harshly lowers user�s Speed.
        """
        pass
