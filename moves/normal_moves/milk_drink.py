from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MilkDrink(Move):
    def __init__(self):
        super().__init__(
            "Milk Drink",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User recovers half its max HP.
        """
        pass
