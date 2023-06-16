from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Purify(Move):
    def __init__(self):
        super().__init__(
            "Purify",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user heals the target's status condition. If the move succeeds, it also restores the user's own HP.
        """
        pass
