import pygame
import math
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT - self.rect.height*2
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.change_x = 5
        elif keys[pygame.K_LEFT]:
            self.change_x = -5
        else:
            self.change_x = 0

        if self.rect.x < 0:
            self.change_x = 0
            self.rect.x = 1
        elif self.rect.x > DISPLAY_WIDTH-self.rect.width:
            self.change_x = 0
            self.rect.x = DISPLAY_WIDTH-self.rect.width-1



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.image = pygame.image.load(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (DISPLAY_WIDTH // 15) * self.x_pos, self.rect.height - y_pos
        self.y_velo = 0
        self.x_velo = 2

    def update(self):
        self.rect.y += self.y_velo
        self.rect.x += self.x_velo
        if self.rect.right >= DISPLAY_WIDTH or self.rect.left <= 0:
            self.x_velo *= -1
            self.rect.y += self.rect.height





class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velo = 2

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y,
                         MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.velo

        if self.rect.bottom <= 0:
            self.kill()

class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y,
                         BLOCK_WIDTH, BLOCK_HEIGHT])


