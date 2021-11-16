import pygame
import math
import random
from settings import *
from sprites import Player, Enemy, Missile

# functions



pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space Invaders")

player_group = pygame.sprite.Group()
player = Player("assets/sprite_ship_3.png")
player_group.add(player)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
