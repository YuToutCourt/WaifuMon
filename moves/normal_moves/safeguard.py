from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Safeguard(Move):
    def __init__(self):
        super().__init__(
            "Safeguard",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user's party is protected from status conditions.
        """
        pass
