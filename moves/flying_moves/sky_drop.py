from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SkyDrop(Move):
    def __init__(self):
        super().__init__(
            "Sky Drop",
            type=TypeFactory.create_type(Types.FLYING),
            power=60,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Takes opponent into the air on first turn, drops them on second turn.
        """
        pass
