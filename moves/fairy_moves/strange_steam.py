from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class StrangeSteam(Move):
    def __init__(self):
        super().__init__(
            "Strange Steam",
            type=TypeFactory.create_type(Types.FAIRY),
            power=90,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self):
        """
        May confuse opponent.
        """
        pass
