import pygame
from pygame.locals import *
import time
import random

boardWidth = 500
boardHeight = 500
snakeAndAppleSize = 20
snakeStartLength = 3
snakeColor = (0, 255, 0)
appleColor = (255, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((boardWidth, boardHeight))
        self.snake = Snake(self.surface, snakeStartLength)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render("Score: {}".format(self.snake.length - snakeStartLength), True, (255, 255, 255))
        self.surface.blit(score, (boardWidth - 120, boardHeight - boardHeight))

    def collision_with_apple(self):
        if self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y:
            self.apple = Apple(self.surface)
            self.snake.increase_length()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.collision_with_apple()
        self.display_score()
        pygame.display.flip()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    self.snake.move_up() if event.key == K_UP \
                        else self.snake.move_down() if event.key == K_DOWN \
                        else self.snake.move_left() if event.key == K_LEFT \
                        else self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.2)


class Snake:
    def __init__(self, surface, length):
        self.block = pygame.Surface((snakeAndAppleSize, snakeAndAppleSize))
        self.block.fill(snakeColor)
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

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "left":
            self.x[0] -= snakeAndAppleSize
        if self.direction == "right":
            self.x[0] += snakeAndAppleSize
        if self.direction == "up":
            self.y[0] -= snakeAndAppleSize
        if self.direction == "down":
            self.y[0] += snakeAndAppleSize
        self.draw()


class Apple:
    def __init__(self, surface):
        self.apple = pygame.Surface((snakeAndAppleSize, snakeAndAppleSize))
        self.apple.fill(appleColor)
        self.surface = surface
        self.x = random.randrange(snakeAndAppleSize, boardWidth - snakeAndAppleSize, snakeAndAppleSize)
        self.y = random.randrange(snakeAndAppleSize, boardWidth - snakeAndAppleSize, snakeAndAppleSize)

    def draw(self):
        self.surface.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
