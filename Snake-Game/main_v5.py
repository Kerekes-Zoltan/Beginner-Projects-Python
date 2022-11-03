"""
Collision detection method
Implement score method on the Top-Right Corner
Little Changes in the Code
"""

import pygame
from pygame.locals import *
import time
import random

SIZE = 30

class Apple:
    def __init__(self, parent_screen) -> None:
        self.parent_screen = parent_screen
        self.image = pygame.image.load("/home/reea/Documents/Python/Snake-Game/images/apple.jpeg").convert()
        self.x = random.randint(0, 25) * SIZE
        self.y = random.randint(0, 20) * SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_random_apple(self):
        self.x = random.randint(0, 25) * SIZE
        self.y = random.randint(0, 20) * SIZE

class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("/home/reea/Documents/Python/Snake-Game/images/block_2.png").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)   #  -1 is the arrays value, to start from 0
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((117, 8, 30))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
            
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((117, 8, 30))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score_()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move_random_apple()

    def score_(self):
        #Python has a font module to help you modify Text
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'Score: {self.snake.length}', True, (255, 255, 255))   #(255, 255, 255) => RGB colors
        self.surface.blit(score, (800, 20)) #Show anything on the surface use Blit Function

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

            self.play()
            time.sleep(.2)

if __name__ == "__main__":
    game = Game()
    game.run()