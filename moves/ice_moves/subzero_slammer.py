from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SubzeroSlammer(Move):
    def __init__(self):
        super().__init__(
            "Subzero Slammer",
            type=TypeFactory.create_type(Types.ICE),
            power=190,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ice type Z-Move.
        """
        pass
