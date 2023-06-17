from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log  import log
from status.poison import Poison

class Twineedle(Move):
    def __init__(self):
        super().__init__(
            "Twineedle",
            type=TypeFactory.create_type(Types.BUG),
            power=25,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=20,
        )

    def effect(self, attacker, defender):
        """
        Hits twice in one turn. May poison opponent.
        """
        defender.status = Poison(defender)
        log("Twineedle", f"{defender.name} is poisoned!")
