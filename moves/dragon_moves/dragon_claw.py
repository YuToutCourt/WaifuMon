from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonClaw(Move):
    def __init__(self):
        super().__init__(
            "Dragon Claw",
            type=TypeFactory.create_type(Types.DRAGON),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass
