from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SilverWind(Move):
    def __init__(self):
        super().__init__(
            "Silver Wind",
            type=TypeFactory.create_type(Types.BUG),
            power=60,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May raise all stats of user at once.
        """
        pass
