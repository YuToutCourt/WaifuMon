import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("asset/Tileset/player.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((34, 177, 76))
        self.rect = self.image.get_rect()
        self.position = (x, y)
        # Vitesse de déplacement du sprite
        self.speed = 0.2
        self.speed_running = 0.4

    def move(self, key_pressed, is_running):
        if is_running:
            self.speed = self.speed_running
        else:
            self.speed = 0.2

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

    def get_image(self, x, y):
        image = pygame.Surface([46, 54])
        image.blit(self.image, (0, 0), (x, y, 46, 54))

        return image