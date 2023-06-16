from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Aromatherapy(Move):
    def __init__(self):
        super().__init__(
            "Aromatherapy",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Cures all status problems in your party.
        """
        pass
