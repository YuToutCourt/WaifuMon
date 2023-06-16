from character.character import Character
from utils.coordinates import Coordinates
from waifu.waifu import Waifu


class NPC(Character):
    def __init__(self, name, coordinates: Coordinates, dialog: str):
        super().__init__(coordinates, "asset/Characters/" + name + ".png")
        self.name = name
        self.dialog = dialog

    def handle_interaction(self, screen, player):
        from game_script.fight_screen import FightScreen

        fight_screen = FightScreen(screen)
        fight_screen.run_fight(player, self)

    def handle_choice_during_fight(self, waifu_player: Waifu, waifu_npc: Waifu):
        # Ajoutez ici le code spécifique à la classe NPC
        return waifu_npc.choice_move()

    def choice_next_waifu(self):
        """
        Change le waifu actif
        """
        import random

        waifu = random.choice(self.get_alive_waifu())
        waifu.in_fight = True
        return waifu
