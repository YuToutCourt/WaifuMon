from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AnchorShot(Move):
    def __init__(self):
        super().__init__(
            "Anchor Shot",
            type=TypeFactory.create_type(Types.STEEL),
            power=80,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user entangles the target with its anchor chain while attacking. The target becomes unable to flee.
        """
        pass
