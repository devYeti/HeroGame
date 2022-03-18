# Game building excersize for Programming Hero course

import pygame


screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')
planet = pygame.image.load('p_one.png')

keep_alive = True
#game loop
while keep_alive:
    screen.blit(background, [0, 0])
    pygame.display.update()
    screen.blit(planet, [140, 50])