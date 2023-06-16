from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Curse(Move):
    def __init__(self):
        super().__init__(
            "Curse",
            type=TypeFactory.create_type(Types.GHOST),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ghosts lose 50% of max HP and curse the opponent; Non-Ghosts raise Attack, Defense and lower Speed.
        """
        pass
