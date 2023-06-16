from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class VoltSwitch(Move):
    def __init__(self):
        super().__init__(
            "Volt Switch",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=70,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User must switch out after attacking.
        """
        pass
