from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SkyAttack(Move):
    def __init__(self):
        super().__init__(
            "Sky Attack",
            type=TypeFactory.create_type(Types.FLYING),
            power=140,
            accuracy=90,
            pp=5,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        Charges on first turn, attacks on second. May cause flinching. High critical hit ratio.
        """
        pass
