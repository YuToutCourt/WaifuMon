from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ShadowClaw(Move):
    def __init__(self):
        super().__init__(
            "Shadow Claw",
            type=TypeFactory.create_type(Types.GHOST),
            power=70,
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
