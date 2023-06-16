from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MeFirst(Move):
    def __init__(self):
        super().__init__(
            "Me First",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User copies the opponent's attack with x1.5 power.
        """
        pass
