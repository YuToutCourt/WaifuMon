from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CottonSpore(Move):
    def __init__(self):
        super().__init__(
            "Cotton Spore",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=40,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Sharply lowers opponent's Speed.
        """
        pass
