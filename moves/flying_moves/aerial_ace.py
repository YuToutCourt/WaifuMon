from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AerialAce(Move):
    def __init__(self):
        super().__init__(
            "Aerial Ace",
            type=TypeFactory.create_type(Types.FLYING),
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
