from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RolePlay(Move):
    def __init__(self):
        super().__init__(
            "Role Play",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User copies the opponent's Ability.
        """
        pass
