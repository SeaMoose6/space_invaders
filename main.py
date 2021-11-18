import pygame
import math
import random
from settings import *
from sprites import Player, Enemy, Missile

# functions



pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space Invaders")

#Sounds
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")

#Sprite Groups
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
missile_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()

player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile = Missile(player.rect.centerx - MISSILE_WIDTH//2, player.rect.top)
                missile_group.add(missile)
                all_sprites.add(missile)
                shoot_sound.play()

    screen.fill(BLACK)

    for string in LAYOUT:
        for val in string:
            if val == 0:
                SPACE_COUNTER += 1
            elif val == 1:
                pass


    #print(missile_group)

    missile_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    missile_group.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
