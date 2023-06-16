from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FellStinger(Move):
    def __init__(self):
        super().__init__(
            "Fell Stinger",
            type=TypeFactory.create_type(Types.BUG),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Drastically raises user's Attack if target is KO'd.
        """
        pass
