from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HealBell(Move):
    def __init__(self):
        super().__init__(
            "Heal Bell",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Heals the user's party's status conditions.
        """
        pass
