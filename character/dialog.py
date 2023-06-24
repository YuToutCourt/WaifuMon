import pygame
import time
from utils.logger import log
class Dialog:

    X_POSITION = 370
    Y_POSITION = 700

    def __init__(self, text):
        box = pygame.image.load("asset/Dialog/dialog_box.png")
        self.box = pygame.transform.scale(box, (800, 100))
        self.font = pygame.font.Font("asset/Dialog/dialog_font.ttf", 20)
        self.texts = [line.strip() for line in text.split("\n") if line.strip()]
        self.text_index = 0
        self.letter_index = 0
        self.reading = True


    def end_dialog(self):
        self.reading = False
        self.text_index = 0


    def display(self, screen):
        
        self.letter_index += 1

        if self.letter_index > len(self.texts[self.text_index]):
            time.sleep(0.5)
            self.next_text()

        screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
        text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
        screen.blit(text, (self.X_POSITION + 70, self.Y_POSITION + 20))


    def next_text(self):
        self.letter_index += 1
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            time.sleep(0.5)
            self.end_dialog()


        
