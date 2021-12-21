import pygame
import math
import random
from settings import *
from sprites import Player, Enemy, Missile, Bomb, Block, Life, Score, Explosion

pygame.init()

LIFE_COUNTER = 3
KILL_COUNTER = 0


def write_file():
    with open('scores.txt', 'w') as high_score:
        high_score.write(f'{KILL_COUNTER}')


def read_file():
    with open('scores.txt') as high_score:
        for score in high_score:
            score = score
        # print(score)

    return score


def start_screen():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.fill(BLACK)
        start_text = BIG_FONT.render("SPACE", True, RED)
        start_text_2 = BIG_FONT.render("INVADERS", True, RED)
        start_text_3 = FONT.render("press SPACE to start", True, WHITE)
        screen.blit(start_text, (275, 300))
        screen.blit(start_text_2, (175, 500))
        screen.blit(start_text_3, (350, 700))



        pygame.display.flip()

        clock.tick(FPS)

def game_over():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        screen.fill(BLACK)
        pygame.display.flip()

        clock.tick(FPS)


def play():
    global KILL_COUNTER
    global LIFE_COUNTER

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Space Invaders")
    print(screen)
    # Sounds
    shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
    enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")

    # Sprite Groups
    player_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    missile_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    life_group = pygame.sprite.Group()
    bomb_group = pygame.sprite.Group()
    other_block_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()

    player = Player("assets/player.png")
    player_group.add(player)
    all_sprites.add(player)

    for num in range(1, 55):
        if num <= 11:
            enemy = Enemy(num, 250, RED_ALIEN, 0)
            enemy_group.add(enemy)
            all_sprites.add(enemy)
        if 10 < num <= 21:
            enemy = Enemy(num - 10, 200, RED_ALIEN, 0)
            enemy_group.add(enemy)
            all_sprites.add(enemy)
        if 20 < num <= 31:
            enemy = Enemy(num - 20, 150, YELLOW_ALIEN, 20)
            enemy_group.add(enemy)
            all_sprites.add(enemy)
        if 30 < num <= 41:
            enemy = Enemy(num - 30, 100, YELLOW_ALIEN, 20)
            enemy_group.add(enemy)
            all_sprites.add(enemy)
        if 40 < num <= 51:
            enemy = Enemy(num - 40, 50, GREEN_ALIEN, 50)
            enemy_group.add(enemy)
            all_sprites.add(enemy)

    SPACE_COUNTER = 0
    ROW_COUNTER = 0

    for num in range(len(LAYOUT)):
        for val in range(len(LAYOUT[num])):
            if LAYOUT[num][val] == "0":
                SPACE_COUNTER += 1
                if SPACE_COUNTER == 50:
                    SPACE_COUNTER = 0
                    ROW_COUNTER += 1
            elif LAYOUT[num][val] == "1":
                SPACE_COUNTER += 1
                block = Block(10 * SPACE_COUNTER, 10 * ROW_COUNTER + 600, screen)
                block_2 = Block(10 * SPACE_COUNTER+450, 10 * ROW_COUNTER + 600, screen)
                block_group.add(block)
                block_group.add(block_2)
                all_sprites.add(block)

    enemy_group.add(enemy)
    all_sprites.add(enemy)
    life_1 = Life(1 * 75, 980)
    life_2 = Life(2 * 75, 980)
    life_3 = Life(3 * 75, 980)
    life_group.add(life_1)
    life_group.add(life_2)
    life_group.add(life_3)

    clock = pygame.time.Clock()
    missile_previous_fire = pygame.time.get_ticks()
    bomb_previous_fire = pygame.time.get_ticks()

    running = True

    enemy_direction = 1



    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    missile_current_fire = pygame.time.get_ticks()
                    if missile_current_fire - missile_previous_fire > MISSILE_DELAY:
                        missile_previous_fire = missile_current_fire
                        missile = Missile(player.rect.centerx - MISSILE_WIDTH // 2, player.rect.top)
                        missile_group.add(missile)
                        all_sprites.add(missile)
                        shoot_sound.play()




        enemy_kills = pygame.sprite.groupcollide(enemy_group, missile_group, True, True)

        if enemy_kills:
            enemy_kill.play()
            for enemy_killed in enemy_kills:
                KILL_COUNTER += 10+enemy_killed.points
            for hit in enemy_kills:
                explosion = Explosion(hit.rect.center)
                explosion_group.add(explosion)
                all_sprites.add(explosion)


        if enemy_group:
            shooting_enemy = list(enemy_group)[random.randint(0, len(enemy_group) - 1)]
            bomb_current_fire = pygame.time.get_ticks()
            if bomb_current_fire - bomb_previous_fire > BOMB_DELAY:
                bomb_previous_fire = bomb_current_fire
                bomb = Bomb(shooting_enemy.rect.x, shooting_enemy.rect.y)
                bomb_group.add(bomb)
                all_sprites.add(bomb)

        pygame.sprite.groupcollide(bomb_group, block_group, True, True)
        pygame.sprite.groupcollide(missile_group, block_group, True, True)
        pygame.sprite.groupcollide(enemy_group, block_group, False, True)

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






        screen.fill(BLACK)

        lives.draw_lives()
        score.draw_score()

        explosion_group.draw(screen)
        other_block_group.draw(screen)
        enemy_group.draw(screen)
        missile_group.draw(screen)
        player_group.draw(screen)
        bomb_group.draw(screen)
        block_group.draw(screen)
        life_group.draw(screen)
        all_sprites.update()

        global h_score

        if LIFE_COUNTER <= -1 or len(enemy_group) == 0:
            h_score = read_file()
            screen.fill(BLACK)
            text = BIG_FONT.render(f"GAME OVER", True, RED)
            text_2 = FONT.render(f"Score: {KILL_COUNTER}", True, WHITE)
            text_3 = FONT.render(f"High score: {h_score}", True, WHITE)
            for missile in missile_group:
                missile.kill()
            screen.blit(text, (200, 400))
            screen.blit(text_2, (415, 600))
            screen.blit(text_3, (400, 750))
            if KILL_COUNTER >= int(h_score):
                write_file()
                text_4 = FONT.render(f"New High Score!", True, WHITE)
                screen.blit(text_4, (400, 800))

        pygame.display.flip()

        clock.tick(FPS)


start_screen()

while True:
    play()
    game_over()

pygame.quit()
