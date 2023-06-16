from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ShellSmash(Move):
    def __init__(self):
        super().__init__("Shell Smash", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Attack, Special Attack and Speed but lowers Defense and Special Defense.
        """
        pass
