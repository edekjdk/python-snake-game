import pygame
from pygame.locals import *

def drawBlock():
    surface.fill((0, 0, 0))
    surface.blit(block, (blockX, blockY))
    pygame.display.flip()


if __name__ == "__main__":

    pygame.init

    surface = pygame.display.set_mode((1000, 500))

    block = pygame.Surface((20, 20))
    block.fill((255, 0, 0))
    blockX = 100
    blockY = 100
    surface.blit(block, (blockX, blockY))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    blockY -= 20
                    drawBlock()
                if event.key == K_DOWN:
                    blockY += 20
                    drawBlock()
                if event.key == K_LEFT:
                    blockX -= 20
                    drawBlock()
                if event.key == K_RIGHT:
                    blockX += 20
                    drawBlock()
            elif event.type == QUIT:
                running = False
