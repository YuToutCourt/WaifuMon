from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PerishSong(Move):
    def __init__(self):
        super().__init__(
            "Perish Song",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Any Pokemon in play when this attack is used faints in 3 turns.
        """
        pass
