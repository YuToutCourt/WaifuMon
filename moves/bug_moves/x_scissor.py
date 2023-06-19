from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class XScissor(Move):
    def __init__(self):
        super().__init__(
            "X-Scissor",
            type=TypeFactory.create_type(Types.BUG),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass
