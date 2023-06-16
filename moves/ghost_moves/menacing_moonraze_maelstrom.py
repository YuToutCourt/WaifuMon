from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MenacingMoonrazeMaelstrom(Move):
    def __init__(self):
        super().__init__(
            "Menacing Moonraze Maelstrom",
            type=TypeFactory.create_type(Types.GHOST),
            power=200,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lunala-exclusive Z-Move.
        """
        pass
