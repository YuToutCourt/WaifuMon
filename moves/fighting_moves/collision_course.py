from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CollisionCourse(Move):
    def __init__(self):
        super().__init__(
            "Collision Course",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=100,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Boosted even more if it's super-effective.
        """
        pass
