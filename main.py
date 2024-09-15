import pygame
from pygame.locals import *
import time
import random


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snakeLength = 1
        self.snake = Snake(self.surface, self.snakeLength)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def displacyScore(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render("Score {}".format(self.snake.length), True, (255, 255, 255))
        self.surface.blit(score, (800, 400))

    def collisionWithApple(self):
        if self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y:
            self.apple = Apple(self.surface)
            self.snake.increaseLenght()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.collisionWithApple()
        self.displacyScore()
        pygame.display.flip()
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

    def increaseLenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

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
        self.x = random.randrange(20, 980, 20)
        self.y = random.randrange(20, 480, 20)

    def draw(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
