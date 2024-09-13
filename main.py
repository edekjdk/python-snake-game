import pygame
from pygame.locals import *


if __name__ == "__main__":
    pygame.init

    surface = pygame.display.set_mode((1000, 500))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                pass
            elif event.type == QUIT:
                running = False