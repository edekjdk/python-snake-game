import pygame
from pygame.locals import *
import time
import random


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface, 10)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            self.play()
            time.sleep(0.2)


class Snake:
    def __init__(self, surface, length):
        self.block = pygame.Surface((20, 20))
        self.block.fill((0, 255, 0))
        self.length = length
        self.x = [100] * self.length
        self.y = [100] * self.length
        self.direction = "right"
        self.surface = surface

    def draw(self):
        self.surface.fill((0, 0, 0))

        for i in range(self.length):
            self.surface.blit(self.block, (self.x[i], self.y[i]))
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

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "left":
            self.x[0] -= 20
        if self.direction == "right":
            self.x[0] += 20
        if self.direction == "up":
            self.y[0] -= 20
        if self.direction == "down":
            self.y[0] += 20
        self.draw()



class Apple:
    def __init__(self, surface):
        self.apple = pygame.Surface((20, 20))
        self.apple.fill((255, 0, 0))
        self.surface = surface
        self.x = random.randint(1, 999)
        self.y = random.randint(1, 499)

    def draw(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
