"""
Implement if the snake hits himself Game Over
Implement Music and sounds
Create Reset function
"""

import pygame
from pygame.locals import *
import time
import random

SIZE = 30
BACKGROUND_COLOR = (117, 8, 30)

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
        self.parent_screen.fill(BACKGROUND_COLOR)
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
        pygame.mixer.init()

        self.play_background_music()
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

    def play_background_music(self):
        pygame.mixer.music.load('/home/reea/Documents/Python/Snake-Game/music/bg_music_1.mp3')
        pygame.mixer.music.play()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score_()
        pygame.display.flip()

        # Snake coliding with apple
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            ding = pygame.mixer.Sound("/home/reea/Documents/Python/Snake-Game/music/ding.mp3")
            pygame.mixer.Sound.play(ding)
            self.snake.increase_length()
            self.apple.move_random_apple()

        # Snake coliding with Himself
        for i in range(1, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                crash = pygame.mixer.Sound("/home/reea/Documents/Python/Snake-Game/music/crash.mp3")
                pygame.mixer.Sound.play(crash)
                raise "Game Over!"

    def score_(self):
        #Python has a font module to help you modify Text
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'Score: {self.snake.length}', True, (255, 255, 255))   #(255, 255, 255) => RGB colors
        self.surface.blit(score, (800, 20)) #Show anything on the surface use Blit Function


    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('Monaco', 40)
        
        line1 = font.render(f'Game over! Your Score was {self.snake.length}', True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))

        line2 = font.render('Press ENTER to play again. Press ESCAPE to Quit', True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()
        pygame.mixer.music.pause()


    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                         running = False
                    
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.2)

if __name__ == "__main__":
    game = Game()
    game.run()