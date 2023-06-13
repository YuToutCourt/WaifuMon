import pygame

from utils.coordinates import Coordinates


class NPC(pygame.sprite.Sprite):
    def __init__(self, name, coordinates: Coordinates, dialog: str):
        super().__init__()
        self.name = name
        self.position = (coordinates.x, coordinates.y)
        self.dialog = dialog
        self.image = pygame.image.load("asset/Characters/" + self.name + ".png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((255, 0, 220))
        self.rect = self.image.get_rect()

    def handle_interaction(self, screen):
        """
        Open a fight screen. That will be closed when the fight ends.
        """
        from game_script.fight_screen import FightScreen

        # print(self.dialog)

        fight_screen = FightScreen(screen)
        fight_screen.fill_screen()
        fight_screen.load_background()

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x: int, y: int):
        """
        Récupère une image dans le spritesheet

        :param x: position x de l'image dans le spritesheet
        :param y: position y de l'image dans le spritesheet

        :return: l'image récupérée
        """
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))

        return image
