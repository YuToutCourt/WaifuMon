from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AttackOrder(Move):
    def __init__(self):
        super().__init__(
            "Attack Order",
            type=TypeFactory.create_type(Types.BUG),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
