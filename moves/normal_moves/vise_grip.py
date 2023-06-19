from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ViseGrip(Move):
    def __init__(self):
        super().__init__(
            "Vise Grip",
            type=TypeFactory.create_type(Types.NORMAL),
            power=55,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass
