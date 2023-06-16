from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Brine(Move):
    def __init__(self):
        super().__init__(
            "Brine",
            type=TypeFactory.create_type(Types.WATER),
            power=65,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power doubles if opponent's HP is less than 50%.
        """
        pass
