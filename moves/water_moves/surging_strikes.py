from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SurgingStrikes(Move):
    def __init__(self):
        super().__init__(
            "Surging Strikes",
            type=TypeFactory.create_type(Types.WATER),
            power=25,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Always results in a critical hit and ignores stat changes.
        """
        pass
