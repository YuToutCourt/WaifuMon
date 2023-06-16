from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FirstImpression(Move):
    def __init__(self):
        super().__init__(
            "First Impression",
            type=TypeFactory.create_type(Types.BUG),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Although this move has great power, it only works the first turn the user is in battle.
        """
        pass
