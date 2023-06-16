from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LusterPurge(Move):
    def __init__(self):
        super().__init__(
            "Luster Purge",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=70,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=50,
        )

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
