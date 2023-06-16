from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ThousandArrows(Move):
    def __init__(self):
        super().__init__(
            "Thousand Arrows",
            type=TypeFactory.create_type(Types.GROUND),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Makes Flying-type Pokemon vulnerable to Ground moves.
        """
        pass
