from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Nothing(Move):
    def __init__(self):
        super().__init__(
            "Nothing",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=0,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
