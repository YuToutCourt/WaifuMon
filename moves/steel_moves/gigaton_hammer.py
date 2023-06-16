from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GigatonHammer(Move):
    def __init__(self):
        super().__init__(
            "Gigaton Hammer",
            type=TypeFactory.create_type(Types.STEEL),
            power=160,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Cannot be used twice in a row.
        """
        pass
