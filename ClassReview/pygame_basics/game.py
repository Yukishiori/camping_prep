import pygame

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
player_image_1 = pygame.image.load('player1.png')
x1 = 0
y1 = 0

player_image_2 = pygame.image.load('player1.png')
y2 = 100
x2 = 100
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
    print(pressed)
    if pressed[pygame.K_UP]: y1 -= 3
    if pressed[pygame.K_DOWN]: y1 += 3
    if pressed[pygame.K_LEFT]: x1 -= 3
    if pressed[pygame.K_RIGHT]: x1 += 3

    (x2, y2) = pygame.mouse.get_pos()

    # Clean canvas
    canvas.fill((200,0,0))

    # 4.2 draw image
    canvas.blit(player_image_1, (x1, y1))
    canvas.blit(player_image_2, (x2, y2))

    clock.tick(60)
    pygame.display.flip() # Back buffer / second buffer

