from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class OrderUp(Move):
    def __init__(self):
        super().__init__(
            "Order Up",
            type=TypeFactory.create_type(Types.DRAGON),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No additional effect.
        """
        pass
