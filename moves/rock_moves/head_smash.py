from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HeadSmash(Move):
    def __init__(self):
        super().__init__(
            "Head Smash",
            type=TypeFactory.create_type(Types.ROCK),
            power=150,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
