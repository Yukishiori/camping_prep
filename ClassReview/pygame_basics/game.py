# import player as player
import pygame
from players.player import Player
from enemies.enemy import Enemy

# ui game minesweeper
# text game
# arcade game
# platformer

# init
pygame.init()

# setup game window
size = (600, 800)  # pixels
canvas = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()
loop = True

# 4.1 load image
player = Player(30, 30)

enemy = Enemy(60,60)
while loop:
    # events

    # quit
    # mouse
    # key
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y1 -= 3
    if pressed[pygame.K_DOWN]: y1 += 3
    if pressed[pygame.K_LEFT]: x1 -= 3
    if pressed[pygame.K_RIGHT]: x1 += 3
    (x2, y2) = pygame.mouse.get_pos()

    player.update()
    enemy.update()
    # Clean canvas
    canvas.fill((200, 0, 0))

    enemy.render(canvas)
    player.render(canvas)

    clock.tick(60)
    pygame.display.flip()  # Back buffer / second buffer
