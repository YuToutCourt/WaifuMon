import pygame

from utils.coordinates import Coordinates

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
        self.team = []

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

    def update(self):
        self.rect.topleft = self.position

    def choice_next_waifu(self):
        """
        Change le waifu actif
        """
        for waifu in self.team:
            if waifu.KO == True or waifu.in_fight == True: continue

            print(waifu.nom)

        # Code à faire pour faire le choix de la waifu
        return self.team[0]
