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
enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")

#Sprite Groups
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
missile_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)


for num in range(1, 55):
    if num <= 11:
        enemy = Enemy(num, 0, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 10 < num <= 21:
        enemy = Enemy(num-10, 50, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 20 < num <= 31:
        enemy = Enemy(num-20, 100, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 30 < num <= 41:
        enemy = Enemy(num-30, 150, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 40 < num <= 51:
        enemy = Enemy(num-40, 200, GREEN_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)

#enemy = Enemy(2, GREEN_ALIEN)
enemy_group.add(enemy)
all_sprites.add(enemy)

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

    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    if enemy_kills:
        enemy_kill.play()

    screen.fill(BLACK)

    for string in LAYOUT:
        for val in string:
            if val == 0:
                SPACE_COUNTER += 1
            elif val == 1:
                pass


    #print(missile_group)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    all_sprites.update()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
