from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MuddyWater(Move):
    def __init__(self):
        super().__init__(
            "Muddy Water",
            type=TypeFactory.create_type(Types.WATER),
            power=90,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
