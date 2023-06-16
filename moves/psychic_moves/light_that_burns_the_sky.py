from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LightThatBurnstheSky(Move):
    def __init__(self):
        super().__init__(
            "Light That Burns the Sky",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=200,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ultra Necrozma-exclusive Z-Move. Ignores target's ability; uses highest Attack stat.
        """
        pass
