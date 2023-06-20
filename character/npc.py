import random

from character.character import Character
from utils.coordinates import Coordinates
from ia.ia import attack_or_switch

class NPC(Character):
    def __init__(self, name, coordinates: Coordinates, dialog: str):
        super().__init__(coordinates, "asset/Characters/" + name + ".png")
        self.name = name
        self.dialog = dialog
        self.speed = 0.2

    def handle_interaction(self, screen, player):
        from game_script.fight_screen import FightScreen

        fight_screen = FightScreen(screen)
        fight_screen.run_fight(player, self)

    def random_move(self):
        new_position = {
            "up": (self.position[0], self.position[1] - self.speed),
            "down": (self.position[0], self.position[1] + self.speed),
            "left": (self.position[0] - self.speed, self.position[1]),
            "right": (self.position[0] + self.speed, self.position[1]),
        }

        direction = random.choice(list(new_position.keys()))

        self.position = new_position[direction]

    def handle_choice_during_fight(self, waifu_player=None, waifu_npc=None, have_to_switch=False):
        
        return attack_or_switch(waifu_npc, waifu_player, self, have_to_switch)

