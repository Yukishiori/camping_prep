# incremental design
# Object management
import pygame
from bullet.bullets import Bullet
import game_object

class Player:
    def __init__(self, x, y, input_manager):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player1.png')
        self.input_manager = input_manager  # reference

    def update(self):
        if self.input_manager.right_pressed:
            self.x += 10
        if self.input_manager.left_pressed:
            self.x -= 10
        if self.input_manager.up_pressed:
            self.y -= 10
        if self.input_manager.down_pressed:
            self.y += 10
        if self.input_manager.x_pressed:
            new_bullet = Bullet(self.x, self.y)
            game_object.add(new_bullet)

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
