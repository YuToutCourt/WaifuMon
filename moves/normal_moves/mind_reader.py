from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MindReader(Move):
    def __init__(self):
        super().__init__(
            "Mind Reader",
            type=TypeFactory.create_type(Types.NORMAL),
            power=150,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User's next attack is guaranteed to hit.
        """
        pass
