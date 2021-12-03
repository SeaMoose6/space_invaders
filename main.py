import pygame
import math
import random
from settings import *
from sprites import Player, Enemy, Missile, Bomb, Block, Life, Score

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
life_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)



for num in range(1, 55):
    if num <= 11:
        enemy = Enemy(num, 200, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 10 < num <= 21:
        enemy = Enemy(num-10, 150, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 20 < num <= 31:
        enemy = Enemy(num-20, 100, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 30 < num <= 41:
        enemy = Enemy(num-30, 50, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 40 < num <= 51:
        enemy = Enemy(num-40, 0, GREEN_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)


    for num in range(len(LAYOUT)):
        for val in range(len(LAYOUT[num])):
            if LAYOUT[num][val] == "0":
                SPACE_COUNTER += 1
                if SPACE_COUNTER == 50:
                    SPACE_COUNTER = 0
                    ROW_COUNTER += 1
            elif LAYOUT[num][val] == "1":
                SPACE_COUNTER += 1
                block = Block(20*SPACE_COUNTER, 50*ROW_COUNTER, screen)
                block_group.add(block)
                all_sprites.add(block)


enemy_group.add(enemy)
all_sprites.add(enemy)
life_1 = Life(1*75, 980)
life_2 = Life(2*75, 980)
life_3 = Life(3*75, 980)
life_group.add(life_1)
life_group.add(life_2)
life_group.add(life_3)



# for num in range(LIFE_COUNTER):
#     life = Life(num*75+30, 980)
#     life_group.add(life)
#     all_sprites.add(life)

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

    shooting_enemy = list(enemy_group)[random.randint(0, len(enemy_group)-1)]
    bomb = Bomb(shooting_enemy.rect.x, shooting_enemy.rect.y)

    pygame.sprite.groupcollide(bomb_group, block_group, True, True)
    pygame.sprite.groupcollide(missile_group, block_group, True, True)

    #print(pygame.sprite.spritecollide(player, bomb_group, True))
    life_kills = pygame.sprite.spritecollide(player, bomb_group, True)
    if life_kills:
        LIFE_COUNTER -= 1
        if LIFE_COUNTER == 2:
            life_3.kill()
        elif LIFE_COUNTER == 1:
            life_2.kill()
        elif LIFE_COUNTER == 0:
            life_1.kill()

    score = Score(FONT, screen)

    # if str(pygame.sprite.spritecollide(player, bomb_group, True)) == '[<Bomb Sprite(in 0 groups)>]':
    #     LIFE_COUNTER -= 1
    #     life.kill()

    if len(bomb_group) < 10:
        bomb_group.add(bomb)
        all_sprites.add(bomb)

    score.draw_score()

    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    bomb_group.draw(screen)
    block_group.draw(screen)
    life_group.draw(screen)
    all_sprites.update()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
