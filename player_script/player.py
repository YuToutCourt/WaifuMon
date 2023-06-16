import pygame
from waifu.waifu import Waifu
from typing import List
from utils.coordinates import Coordinates
from wtypes.type_factory import TypeFactory
from utils.handle_input import input_int

class Player(pygame.sprite.Sprite):
    def __init__(self, coordinates:Coordinates):
        super().__init__()
        self.image = pygame.image.load("asset/Characters/player.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((255, 0, 220))
        self.rect = self.image.get_rect()
        self.position = (coordinates.x, coordinates.y)
        # Vitesse de déplacement du sprite
        self.speed = 0.4
        self.speed_running = 0.6
        self.team: List[Waifu] = []
        self.__create_random_team()

    def get_image(self, x:int, y:int):
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))

        return image

    def move(self, key_pressed, is_running: bool):
        """
        Déplace le joueur en fonction des touches pressées
        :param key_pressed: touches pressées
        :param is_running: si le joueur court ou non
        """
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
        Déplace le joueur en arrière en fonction de la direction
        """
        if direction == "down":
            self.position = (self.position[0], self.position[1] + self.speed)
        if direction == "up":
            self.position = (self.position[0], self.position[1] - self.speed)
        if direction == "right":
            self.position = (self.position[0] + self.speed, self.position[1])
        if direction == "left":
            self.position = (self.position[0] - self.speed, self.position[1])
        if direction == "surprise":
            self.position = (self.position[0] - self.speed, self.position[1])

    def update(self):
        self.rect.topleft = self.position

    def print_team(self):
        """
        Affiche les waifus du joueur
        """
        for waifu in self.team:
            print(waifu.name)

    def get_waifu_in_fight(self):
        """
        Récupère le waifu actif
        """
        for waifu in self.team:
            if waifu.in_fight:
                return waifu
        return None

    def get_alive_waifu(self):
        """
        Récupère les waifus en vie
        """
        return [waifu for waifu in self.team if waifu.KO == False]

    def choice_next_waifu(self):
        """
        Change le waifu actif
        """
        alive_waifu = self.get_alive_waifu()
        for index, waifu in enumerate(alive_waifu):
            print(f"{index} {waifu.name}")
        
        choice = input_int("Choisissez un waifu: ", 0, len(alive_waifu) - 1)
            
        waifu = alive_waifu[choice]
        waifu.in_fight = True

        return waifu

    def __create_random_team(self):
        """
        Crée une équipe de 6 waifu aléatoire
        """
        from random import shuffle, randint
        with open("asset/waifu_sprite/all_waifu_name.txt", "r", encoding="utf-8") as file:
            data = file.read().split("\n")
            shuffle(data)
            for w in data[:6]:
                name, types, id = w.split(",")
                types = types.split("-")
                types_ = []
                for type in types:
                   types_.append(TypeFactory.create_type(type))

                waifu = Waifu(
                    id,
                    name,
                    randint(50, 200),
                    randint(50, 200),
                    randint(50, 200),
                    randint(50, 100),
                    types_,
                    randint(1, 100)
                )
                self.team.append(waifu)