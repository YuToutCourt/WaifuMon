from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MetalClaw(Move):
    def __init__(self):
        super().__init__(
            "Metal Claw",
            type=TypeFactory.create_type(Types.STEEL),
            power=50,
            accuracy=95,
            pp=35,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May raise user's Attack.
        """
        pass
