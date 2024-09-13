import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.moveUp()
                    if event.key == K_DOWN:
                        self.snake.moveDown()

                    if event.key == K_LEFT:
                        self.snake.moveLeft()

                    if event.key == K_RIGHT:
                        self.snake.moveRight()

                elif event.type == QUIT:
                    running = False


class Snake:
    def __init__(self, surface):
        self.block = pygame.Surface((20, 20))
        self.block.fill((255, 0, 0))
        self.x = 100
        self.y = 100
        self.surface = surface

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def moveUp(self):
        self.y -= 20
        self.draw()

    def moveDown(self):
        self.y += 20
        self.draw()

    def moveLeft(self):
        self.x -= 20
        self.draw()

    def moveRight(self):
        self.x += 20
        self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
