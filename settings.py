import pygame
import math
import random

pygame.init()

# constants
YELLOW = (219, 150, 31)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 77, 0)
BLOCK_COLOR = (252, 53, 3)

EXPLOSION_LIST = []
for i in range(8):
    image_path = pygame.image.load(f'assets/sprite_{i}.png')
    EXPLOSION_LIST.append(image_path)

FONT = pygame.font.Font("assets/unifont.ttf", 25)
BIG_FONT = pygame.font.Font("assets/unifont.ttf", 150)
PI = math.pi

DISPLAY_HEIGHT = 1000
DISPLAY_WIDTH = 1000
SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

MISSILE_WIDTH = 4
MISSILE_HEIGHT = 15
BLOCK_WIDTH = 10
BLOCK_HEIGHT = 10
MISSILE_DELAY = 300
BOMB_DELAY = 300
FPS = 120

PLAYER = "assets/player.png"
RED_ALIEN = "assets/red.png"
GREEN_ALIEN = "assets/green.png"
YELLOW_ALIEN = "assets/yellow.png"

LAYOUT = ["00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000001111111000000000000000011111110000000000",
          "00000000011111111100000000000000111111111000000000",
          "00000000111111111110000000000001111111111100000000",
          "00000000111111111110000000000001111111111100000000",
          "00000000111111111110000000000001111111111100000000",
          "00000000111000001110000000000001110000011100000000",
          "00000000110000000110000000000001100000001100000000",
          "00000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000",

          ]

SHIELD = '''
  1111111
 111111111
11111111111
11111111111
11111111111
111     111
11       11
'''

h_scale = len(LAYOUT)
v_scale = len(LAYOUT[0])
