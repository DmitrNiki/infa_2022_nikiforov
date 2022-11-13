import pygame
from pygame.draw import *
from random import randint

pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 1
screen = pygame.display.set_mode((900, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
counter = 0


class Ball:
    __x = 0
    __y = 0
    __r = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_r(self):
        return self.__r

    def new_ball(self):
        '''рисует новый шарик '''

        self.__x = randint(100, 700)
        self.__y = randint(100, 500)
        self.__r = randint(30, 50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (self.__x, self.__y), self.__r)


def isCaught(event, x, y, r):
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 < r ** 2:
        print('Caught!')
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False
ball1 = Ball()
ball2 = Ball()

while not finished:
    clock.tick(FPS)
    flag = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if flag == 0 and (isCaught(event, ball1.get_x(), ball1.get_y(), ball1.get_r()) or isCaught(event, ball2.get_x(),
                                                                                        ball2.get_y(), ball2.get_r())):
                counter += 1
                flag = 1

    text_surface = my_font.render(f'COUNTER: {counter}', False, (255, 255, 255))
    ball1.new_ball()
    ball2.new_ball()
    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(text_surface, (50, 50))

pygame.quit()