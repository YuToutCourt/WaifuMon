from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Growth(Move):
    def __init__(self):
        super().__init__(
            "Growth",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack and Special Attack.
        """
        pass
