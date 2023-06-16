from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SimpleBeam(Move):
    def __init__(self):
        super().__init__(
            "Simple Beam",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Changes target's ability to Simple.
        """
        pass
