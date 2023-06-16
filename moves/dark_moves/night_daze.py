from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class NightDaze(Move):
    def __init__(self):
        super().__init__(
            "Night Daze",
            type=TypeFactory.create_type(Types.DARK),
            power=85,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=40,
        )

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
