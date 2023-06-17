from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BugBuzz(Move):
    def __init__(self):
        super().__init__(
            "Bug Buzz",
            type=TypeFactory.create_type(Types.BUG),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May lower opponent's Special Defense.
        """
        self.set_waifu_reciver(waifu_reciver)

        
