from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Acid(Move):
    def __init__(self):
        super().__init__(
            "Acid",
            type=TypeFactory.create_type(Types.POISON),
            power=40,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
