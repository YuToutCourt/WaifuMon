import random

from character.character import Character
from utils.coordinates import Coordinates
from ia.ia import attack_or_switch
from character.dialog import Dialog
import pygame
import time

# TODO : Create a class for each NPC that inherit from NPC
# Because each NPC will have a different behavior


class NPC(Character):
    def __init__(self, name, coordinates: Coordinates, dialog: str):
        super().__init__(coordinates, "asset/Characters/" + name + ".png")
        self.name = name
        self.dialog = Dialog(dialog)
        self.speed = 0.2
        self.target_position = None
        

    def handle_interaction(self, screen, player):
        """
        Handle the interaction with the NPC
        """
        from game_script.fight_screen import FightScreen

        while self.dialog.reading:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.dialog.end_dialog()

            self.dialog.display(screen)
            pygame.display.flip()
            time.sleep(0.05)


        fight_screen = FightScreen(screen)
        fight_screen.run_fight(player, self)

    def handle_choice_during_fight(self, waifu_player=None, waifu_npc=None, have_to_switch=False):
        """
        Handle the choice of the NPC during the fight
        """
        return attack_or_switch(waifu_npc, waifu_player, self, have_to_switch)

    def random_move(self, collisions):
        if self.target_position is None or self.position == self.target_position:
            self.target_position = self.generate_random_position()

        direction_vector = (
            self.target_position[0] - self.position[0],
            self.target_position[1] - self.position[1]
        )

        direction_length = (direction_vector[0] ** 2 + direction_vector[1] ** 2) ** 0.5

        if direction_length > self.speed:
            normalized_direction = (
                direction_vector[0] / direction_length,
                direction_vector[1] / direction_length
            )
            movement = (
                normalized_direction[0] * self.speed,
                normalized_direction[1] * self.speed
            )
        else:
            movement = direction_vector

        self.position = (
            self.position[0] + movement[0],
            self.position[1] + movement[1]
        )
        for collision in collisions:
            if pygame.Rect(self.position[0], self.position[1], 32,32 ).colliderect(collision):
                self.move_back(movement)
                self.target_position = self.generate_random_position()


    def move_back(self, movement):
        self.position = (
            self.position[0] - movement[0],
            self.position[1] - movement[1]
        )


    def generate_random_position(self):
        """
        Generate a random position for the NPC
        """
        min_x, max_x = 18, 800
        min_y, max_y = 200, 700


        return random.uniform(min_x, max_x), random.uniform(min_y, max_y)

