"""
Snake game using Pygame module
Creating the window, Quit Key
Background and The Block to Move
"""

import pygame
from pygame.locals import *


def draw_block():
    surface.fill((117, 8, 30))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()
    


if __name__ == "__main__":
    pygame.init()

    #Set up the game window
    surface = pygame.display.set_mode((1000, 1000))

    #Fill function will fill the background of the Game
    surface.fill((117, 8, 30))
    
    block = pygame.image.load("/home/reea/Documents/Python/Snake-Game/images/block_2.png").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False