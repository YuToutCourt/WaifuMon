from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GenesisSupernova(Move):
    def __init__(self):
        super().__init__(
            "Genesis Supernova",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=185,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Mew-exclusive Z-Move.
        """
        pass
