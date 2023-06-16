from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RockClimb(Move):
    def __init__(self):
        super().__init__(
            "Rock Climb",
            type=TypeFactory.create_type(Types.NORMAL),
            power=90,
            accuracy=85,
            pp=20,
            priority=0,
            proba_effect=20,
        )

    def effect(self):
        """
        May confuse opponent.
        """
        pass
