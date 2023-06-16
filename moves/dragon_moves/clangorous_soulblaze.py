from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ClangorousSoulblaze(Move):
    def __init__(self):
        super().__init__(
            "Clangorous Soulblaze",
            type=TypeFactory.create_type(Types.DRAGON),
            power=185,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Kommo-o exclusive Z-Move.
        """
        pass
