from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BloomDoom(Move):
    def __init__(self):
        super().__init__(
            "Bloom Doom",
            type=TypeFactory.create_type(Types.GRASS),
            power=180,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Grass type Z-Move.
        """
        pass
