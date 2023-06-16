from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CorkscrewCrash(Move):
    def __init__(self):
        super().__init__(
            "Corkscrew Crash",
            type=TypeFactory.create_type(Types.STEEL),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Steel type Z-Move.
        """
        pass
