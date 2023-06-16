from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SpectralThief(Move):
    def __init__(self):
        super().__init__(
            "Spectral Thief",
            type=TypeFactory.create_type(Types.GHOST),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user hides in the target's shadow, steals the target's stat boosts, and then attacks.
        """
        pass
