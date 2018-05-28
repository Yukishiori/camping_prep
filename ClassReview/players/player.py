# incremental design
# Object management
import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player1.png')

    def update(self):
        pass

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
