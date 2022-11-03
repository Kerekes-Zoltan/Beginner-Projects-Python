"""
From Version_1 I learned to create a basic running Game
Version 2, focused to convert it to OOP
"""

import pygame
from pygame.locals import *


class Snake:
    def __init__(self, parent_screen) -> None:
        self.parent_screen = parent_screen
        self.block = pygame.image.load("/home/reea/Documents/Python/Snake-Game/images/block_2.png").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((117, 8, 30))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((117, 8, 30))
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
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()