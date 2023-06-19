from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Retaliate(Move):
    def __init__(self):
        super().__init__(
            "Retaliate",
            type=TypeFactory.create_type(Types.NORMAL),
            power=140,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Inflicts double damage if a teammate fainted on the last turn.
        """
        pass
