from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MeteorMash(Move):
    def __init__(self):
        super().__init__(
            "Meteor Mash",
            type=TypeFactory.create_type(Types.STEEL),
            power=90,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self):
        """
        May raise user's Attack.
        """
        pass
