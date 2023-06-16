from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HyperspaceHole(Move):
    def __init__(self):
        super().__init__(
            "Hyperspace Hole",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Can strike through Protect/Detect.
        """
        pass
