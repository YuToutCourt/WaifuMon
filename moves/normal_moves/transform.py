from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Transform(Move):
    def __init__(self):
        super().__init__(
            "Transform",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User takes on the form and attacks of the opponent.
        """
        pass
