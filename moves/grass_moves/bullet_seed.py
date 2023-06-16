from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BulletSeed(Move):
    def __init__(self):
        super().__init__(
            "Bullet Seed",
            type=TypeFactory.create_type(Types.GRASS),
            power=25,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
