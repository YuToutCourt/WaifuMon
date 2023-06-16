from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WaveCrash(Move):
    def __init__(self):
        super().__init__(
            "Wave Crash",
            type=TypeFactory.create_type(Types.WATER),
            power=120,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
