from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ClangorousSoul(Move):
    def __init__(self):
        super().__init__("Clangorous Soul", type=TypeFactory.create_type(Types.DRAGON), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises all user's stats but loses HP.
        """
        pass
