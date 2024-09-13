import pygame
from pygame.locals import *
import time


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

                    self.snake.moveUp() if event.key == K_UP \
                        else self.snake.moveDown() if event.key == K_DOWN \
                        else self.snake.moveLeft() if event.key == K_LEFT \
                        else self.snake.moveRight()


                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)


class Snake:
    def __init__(self, surface):
        self.block = pygame.Surface((20, 20))
        self.block.fill((255, 0, 0))
        self.x = 100
        self.y = 100
        self.direction = "left"
        self.surface = surface

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def moveUp(self):
        self.direction = "up"

    def moveDown(self):
        self.direction = "down"

    def moveLeft(self):
        self.direction = "left"

    def moveRight(self):
        self.direction = "right"

    def walk(self):
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
            self.y += 10
        self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
