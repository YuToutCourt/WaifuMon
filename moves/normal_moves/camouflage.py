from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Camouflage(Move):
    def __init__(self):
        super().__init__(
            "Camouflage",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Changes user's type randomly.
        """
        from random import choice

        random_type = TypeFactory.create_type(choice(list(Types)))

        waifu_user.types.clear()
        waifu_user.types.append(random_type)
        log(self.name, "changes", waifu_user.name, "type to", random_type.name)
