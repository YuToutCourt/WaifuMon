from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AuroraBeam(Move):
    def __init__(self):
        super().__init__(
            "Aurora Beam",
            type=TypeFactory.create_type(Types.ICE),
            power=85,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        No effect.
        """
        pass
