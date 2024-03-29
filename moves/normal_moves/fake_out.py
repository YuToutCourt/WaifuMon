from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FakeOut(Move):
    def __init__(self):
        super().__init__(
            "Fake Out",
            type=TypeFactory.create_type(Types.NORMAL),
            power=40,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User attacks first, foe flinches. Only usable on first turn.
        """
        pass
