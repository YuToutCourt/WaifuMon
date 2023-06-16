from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ShoreUp(Move):
    def __init__(self):
        super().__init__(
            "Shore Up",
            type=TypeFactory.create_type(Types.GROUND),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user regains up to half of its max HP. It restores more HP in a sandstorm.
        """
        pass
