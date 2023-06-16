from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MysticalPower(Move):
    def __init__(self):
        super().__init__(
            "Mystical Power",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=70,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack or Defense.
        """
        pass
