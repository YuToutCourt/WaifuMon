from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BouncyBubble(Move):
    def __init__(self):
        super().__init__(
            "Bouncy Bubble",
            type=TypeFactory.create_type(Types.WATER),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass
