from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Tailwind(Move):
    def __init__(self):
        super().__init__(
            "Tailwind",
            type=TypeFactory.create_type(Types.FLYING),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Doubles Speed for 4 turns.
        """
        pass
