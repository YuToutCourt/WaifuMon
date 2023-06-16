from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AquaJet(Move):
    def __init__(self):
        super().__init__(
            "Aqua Jet",
            type=TypeFactory.create_type(Types.WATER),
            power=40,
            accuracy=100,
            pp=20,
            priority=1,
            proba_effect=100,
        )

    def effect(self):
        """
        User attacks first.
        """
        pass
