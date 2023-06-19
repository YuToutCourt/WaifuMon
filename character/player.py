import pygame

from character.character import Character
from utils.coordinates import Coordinates
from utils.handle_input import input_int
from status.status import StatusE


class Player(Character):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates, "asset/Characters/player.png")
        self.speed = 0.4
        self.speed_running = 0.6

    def move(self, key_pressed, is_running: bool):
        if is_running:
            self.speed = self.speed_running

        if key_pressed[pygame.K_UP]:
            self.position = (self.position[0], self.position[1] - self.speed)
        if key_pressed[pygame.K_DOWN]:
            self.position = (self.position[0], self.position[1] + self.speed)
        if key_pressed[pygame.K_LEFT]:
            self.position = (self.position[0] - self.speed, self.position[1])
        if key_pressed[pygame.K_RIGHT]:
            self.position = (self.position[0] + self.speed, self.position[1])

    def move_back(self, direction: str):
        """
        Déplace le joueur en fonction des touches pressées
        :param: direction : direction du mouvement
        """
        direction_map = {
            "down": (0, self.speed),
            "up": (0, -self.speed),
            "right": (self.speed, 0),
            "left": (-self.speed, 0),
            "down_right": (self.speed, self.speed),
            "down_left": (-self.speed, self.speed),
            "up_right": (self.speed, -self.speed),
            "up_left": (-self.speed, -self.speed),
            "surprise": (-self.speed, 0),
        }

        if direction in direction_map:
            offset = direction_map[direction]
            self.position = (self.position[0] + offset[0], self.position[1] + offset[1])

    def choice_next_waifu(self, current_waifu):
        alive_waifu = self.get_alive_waifu()

        for index, waifu in enumerate(alive_waifu):
            print(f"{index} {waifu.name}")

        choice = input_int("Choisissez un waifu: ", 0, len(alive_waifu) - 1)

        current_waifu.in_fight = False

        # Clean confusions and stats change
        if current_waifu.status == StatusE.CONFUSE:
            current_waifu.status = None
        
        current_waifu.attack = current_waifu.base_attack
        current_waifu.defense = current_waifu.base_defense
        current_waifu.speed = current_waifu.base_speed

        waifu = alive_waifu[choice]
        waifu.in_fight = True

        return waifu