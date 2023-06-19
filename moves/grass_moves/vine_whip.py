from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class VineWhip(Move):
    def __init__(self):
        super().__init__(
            "Vine Whip",
            type=TypeFactory.create_type(Types.GRASS),
            power=45,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass
