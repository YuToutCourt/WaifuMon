from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LunarBlessing(Move):
    def __init__(self):
        super().__init__(
            "Lunar Blessing",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Heals user's status conditions and recovers HP.
        """
        pass
