from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TripleAxel(Move):
    def __init__(self):
        super().__init__(
            "Triple Axel",
            type=TypeFactory.create_type(Types.ICE),
            power=20,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Attacks thrice with more power each time.
        """
        pass
