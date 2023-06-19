from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class FloralHealing(Move):
    def __init__(self):
        super().__init__(
            "Floral Healing",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The user restores the target's HP by up to half of its max HP. It restores more HP when the user has the Grass Types
        """
        if waifu_receiver.hp == waifu_receiver.hp_max:
            log(waifu_receiver.name, "is already full hp")
        else:
            if any(Types.GRASS == type_.type_name for type_ in waifu_user.types):
                waifu_receiver.hp += waifu_receiver.hp_max * 0.75
                if waifu_receiver.hp > waifu_receiver.hp_max:
                    waifu_receiver.hp = waifu_receiver.hp_max
                log(waifu_receiver.name, "has recovered a lot of HP")
            else:
                waifu_receiver.hp += waifu_receiver.hp_max * 0.5
                if waifu_receiver.hp > waifu_receiver.hp_max:
                    waifu_receiver.hp = waifu_receiver.hp_max
                log(waifu_receiver.name, "has recovered HP")
