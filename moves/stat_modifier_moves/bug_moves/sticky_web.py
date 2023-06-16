from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class StickyWeb(Move):
    def __init__(self):
        super().__init__(
            "Sticky Web",
            type=TypeFactory.create_type(Types.BUG),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Speed when switching into battle.
        """
        pass
