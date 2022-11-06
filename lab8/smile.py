import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (235, 235, 235), (0, 0, 400, 400))
circle(screen, (255, 209, 64), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)
circle(screen, (255, 0, 0), (155, 175), 20)
circle(screen, (0, 0, 0), (155, 175), 20, 2)
circle(screen, (0, 0, 0), (155, 175), 8)
circle(screen, (255, 0, 0), (245, 175), 15)
circle(screen, (0, 0, 0), (245, 175), 15, 2)
circle(screen, (0, 0, 0), (245, 175), 7)
rect(screen, (0, 0, 0), (150, 240, 100, 25))
polygon(screen, (0, 0, 0), [(100, 100), (180, 165)], 15)
polygon(screen, (0, 0, 0), [(220, 165), (310, 120)], 15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            finished = True

pygame.quit()