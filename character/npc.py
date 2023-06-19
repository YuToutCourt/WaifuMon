import random

from character.character import Character
from utils.coordinates import Coordinates
from waifu.waifu import Waifu
from utils.logger import log
from moves.move_factory import MoveFactory
from moves.enum_moves import Moves
from status.status import StatusE

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

    def handle_choice_during_fight(self, waifu_player: Waifu, waifu_npc: Waifu):
        # Ajoutez ici le code spécifique à la classe NPC

        if all(move.pp <= 0 for move in waifu_npc.list_of_moves):
            log("NPC PP", "Not enough PP, your waifu use struggle")
            waifu_npc.move_to_use = MoveFactory.create_move(Moves.STRUGGLE)
            return waifu_npc.move_to_use

        while True:
            move = random.choice(waifu_npc.list_of_moves)
            if move.pp > 0:
                waifu_npc.move_to_use = move
                waifu_npc.move_to_use.pp -= 1
                return waifu_npc.move_to_use

    def choice_next_waifu(self, current_waifu: Waifu):
        """
        Change le waifu actif
        """
        current_waifu.in_fight = False

        # Clean confusions and stats change
        if current_waifu.status == StatusE.CONFUSE:
            current_waifu.status = None
        
        current_waifu.attack = current_waifu.base_attack
        current_waifu.defense = current_waifu.base_defense
        current_waifu.speed = current_waifu.base_speed

        waifu = random.choice(self.get_alive_waifu())
        waifu.in_fight = True
        return waifu
