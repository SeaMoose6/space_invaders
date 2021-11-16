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



class Enemy():
    pass


class Missile():
    pass
