import pygame
import math

#in terminal "pip install pygame"

pygame.init()

# constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


PI = math.pi

SIZE = (1000, 750)
FPS = 60


# functions



pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Beach")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
