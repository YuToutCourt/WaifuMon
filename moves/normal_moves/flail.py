from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Flail(Move):
    def __init__(self):
        super().__init__(
            "Flail",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The lower the user's HP, the higher the power.
        """
        pass
