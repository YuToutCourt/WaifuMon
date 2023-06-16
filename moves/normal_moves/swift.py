from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Swift(Move):
    def __init__(self):
        super().__init__(
            "Swift",
            type=TypeFactory.create_type(Types.NORMAL),
            power=60,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass
