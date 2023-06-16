from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ClearSmog(Move):
    def __init__(self):
        super().__init__(
            "Clear Smog",
            type=TypeFactory.create_type(Types.POISON),
            power=50,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Removes all of the target's stat changes.
        """
        pass
