# import player as player
import pygame
from players.player import Player
from enemies.enemy import Enemy
from inputs.inputs_manager import InputManager
import game_object

pygame.init()

# setup game window
size = (600, 800)  # pixels
canvas = pygame.display.set_mode(size)
input_manager = InputManager()
# Clock
clock = pygame.time.Clock()
loop = True

player = Player(30, 30, input_manager)
enemy = Enemy(60, 60)

game_object.add(player)
game_object.add(enemy)

while loop:
    # events

    # quit
    # mouse
    # key
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()
    # Clean canvas
    canvas.fill((200, 0, 200))

    game_object.render(canvas)

    clock.tick(60)
    pygame.display.flip()  # Back buffer / second buffer
