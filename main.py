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
other_block_group = pygame.sprite.Group()

player = Player("assets/player.png")
player_group.add(player)
all_sprites.add(player)



for num in range(1, 55):
    if num <= 11:
        enemy = Enemy(num, 250, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 10 < num <= 21:
        enemy = Enemy(num-10, 200, RED_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 20 < num <= 31:
        enemy = Enemy(num-20, 150, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 30 < num <= 41:
        enemy = Enemy(num-30, 100, YELLOW_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
    if 40 < num <= 51:
        enemy = Enemy(num-40, 50, GREEN_ALIEN)
        enemy_group.add(enemy)
        all_sprites.add(enemy)
# #
# x_offset = 30
# y_offset = 60
# for row in range(6):
#     if row == 1: enemy_img = RED_ALIEN
#     elif 1 < row < 4 : enemy_img = GREEN_ALIEN
#     else: enemy_img = YELLOW_ALIEN
#
#     for col in range(11):
#         x_pos = col*h_scale+x_offset
#         y_pos = row+v_scale+y_offset
#         enemy = Enemy(enemy_img, x_pos, y_pos)
#         enemy_group.add(enemy)

for num in range(len(LAYOUT)):
    for val in range(len(LAYOUT[num])):
        if LAYOUT[num][val] == "0":
            SPACE_COUNTER += 1
            if SPACE_COUNTER == 50:
                SPACE_COUNTER = 0
                ROW_COUNTER += 1
        elif LAYOUT[num][val] == "1":
            SPACE_COUNTER += 1
            block = Block(20*SPACE_COUNTER, 30*ROW_COUNTER+200, screen)
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

# for row_index, row in enumerate(SHIELD):
#     #print(row_index, row)
#     for col_index, col in enumerate(row):
#         if col == 'x':
#             x_pos = col_index
#             y_pos = row_index
#             block = Other_Blocks(screen, x_pos, y_pos)
#             other_block_group.add(block)


clock = pygame.time.Clock()
missile_previous_fire = pygame.time.get_ticks()

running = True

enemy_direction = 1

while running:
    def write_file():
        with open('scores.txt', 'w') as high_score:
                high_score.write(f'{KILL_COUNTER}')

    def read_file():
        with open('scores.txt') as high_score:
            for score in high_score:
                score = score
            #print(score)

        return score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile_current_fire = pygame.time.get_ticks()
                if missile_current_fire - missile_previous_fire > MISSILE_DELAY:
                    missile_previous_fire = missile_current_fire
                    missile = Missile(player.rect.centerx - MISSILE_WIDTH//2, player.rect.top)
                    missile_group.add(missile)
                    all_sprites.add(missile)
                    shoot_sound.play()



    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    if enemy_kills:
        enemy_kill.play()
        KILL_COUNTER += 1
    #print(len(enemy_group))
    # enemies = enemy_group.sprites()
    # for enemy in enemies:
    #     if enemy.rect.right >= DISPLAY_WIDTH:
    #         enemy_direction = -1
    #
    #     elif enemy.rect.x <= 0:
    #         enemy_direction = 1

    screen.fill(BLACK)
    if enemy_group:
        shooting_enemy = list(enemy_group)[random.randint(0, len(enemy_group)-1)]
        bomb = Bomb(shooting_enemy.rect.x, shooting_enemy.rect.y)

    pygame.sprite.groupcollide(bomb_group, block_group, True, True)
    pygame.sprite.groupcollide(missile_group, block_group, True, True)

    life_kills = pygame.sprite.spritecollide(player, bomb_group, True)
    if life_kills:
        LIFE_COUNTER -= 1
        if LIFE_COUNTER == 2:
            life_3.kill()
        elif LIFE_COUNTER == 1:
            life_2.kill()
        elif LIFE_COUNTER == 0:
            life_1.kill()

    lives = Score(FONT, screen, LIFE_COUNTER, 300, 20)
    score = Score(FONT, screen, KILL_COUNTER, 50, 20)

    if len(bomb_group) < 10:
        bomb_group.add(bomb)
        all_sprites.add(bomb)

    lives.draw_lives()
    score.draw_score()

    other_block_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    bomb_group.draw(screen)
    block_group.draw(screen)
    life_group.draw(screen)
    all_sprites.update()

    if LIFE_COUNTER <= -1 or len(enemy_group) == 0:
        high_score = read_file()
        screen.fill(BLACK)
        text = BIG_FONT.render(f"GAME OVER", True, RED)
        text_2 = FONT.render(f"Score: {KILL_COUNTER}", True, WHITE)
        text_3 = FONT.render(f"High score: {high_score}", True, WHITE)
        text_4 = FONT.render(f"New High Score!", True, WHITE)
        for missile in missile_group:
            missile.kill()
        screen.blit(text, (200, 400))
        screen.blit(text_2, (415 ,  600))
        screen.blit(text_3, (400, 750))
        #screen.blit(text_4, (400, 775))
        if KILL_COUNTER > int(high_score):
            write_file()
            screen.blit(text_4, (400, 775))
            print('not bugged')




    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
