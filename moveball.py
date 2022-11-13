import pygame
from random import randint
from random import choice


pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 30
WIDTH = 1000
HIGHT = 700
screen = pygame.display.set_mode((WIDTH, HIGHT))

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
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = randint(100, WIDTH-100)
        self.y = randint(100, HIGHT-100)
        self.r = randint(30, 50)
        self.vx = randint(-10,10)
        self.vy = randint(-10,10)
        self.color = choice(COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        '''
        Функция рисует шарик
        '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self):
        """Функция проверяет, сталкивалкивается ли шарик со стеной.

        Returns:
            Возвращает True в случае столкновения мяча и стены. В противном случае возвращает False.
        """
        delta = 1
        if (self.y > self.r + delta) and (self.y < HIGHT - self.r - delta) and (self.x > self.r + delta) and (
                self.x < WIDTH - self.r - delta):
            return False
        else:
            return True

    def fix_position(self):
        '''
        Исправляет позицию шарика при коллизии,
        чтобы избежать проблем, связанных в краевыми эффектами
        '''
        delta1 = 5
        if self.x < delta1 + self.r:
            self.x = delta1 + self.r
        if self.x > WIDTH - self.r - delta1:
            self.x = WIDTH - self.r - delta1
        if self.y < delta1 + self.r:
            self.y = delta1 + self.r
        if self.y > HIGHT - self.r - delta1:
            self.y = HIGHT - self.r - delta1

    def rand_v(self):
        '''
        Функция генерирует рандомную скорость и меняет ее у шарика
        в зависимости от его положения(с какой именно стеной он столкнулся)
        '''
        if (self.x < self.r + 10) and (self.y < self.r + 10) or (self.x > WIDTH - self.r - 10) and (
                self.y > HIGHT - self.r - 10) or (self.x < self.r + 10) and (self.y > HIGHT - self.r - 10) or (
                self.x > WIDTH - self.r - 10) and (self.y < self.r + 10):
            if self.vx < 0:
                if self.vy < 0:
                    self.vx = randint(5, 10)
                    self.vy = randint(5, 10)
                else:
                    self.vx = randint(5, 10)
                    self.vy = randint(-10, -5)
            else:
                if self.vy < 0:
                    self.vx = randint(-10, -5)
                    self.vy = randint(5, 10)
                else:
                    self.vx = randint(-10, -5)
                    self.vy = randint(-10, -5)
        elif self.x < self.r + 10:
            self.vx = randint(5, 10)
            self.vy = randint(-10, 10)
        elif self.y < self.r + 10:
            self.vy = randint(5, 10)
            self.vx = randint(-10, 10)
        elif self.x > WIDTH - self.r - 10:
            self.vx = randint(-10, -5)
            self.vy = randint(-10, 10)
        elif self.y > HIGHT - self.r - 10:
            self.vy = randint(-10, -5)
            self.vx = randint(-10, 10)

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_r(self):
        return self.r

def isCaught(event, x, y, r):
    """Функция проверяет, попала ли мышь в шарик.

            Args:
                event: событие мыши.
                x, y: координаты шарика
                r: радиус шарика
            Returns:
                Возвращает True в попадания мыши в шарик. В противном случае возвращает False.
    """
    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 < r ** 2:
        return True
    else:
        return False


pygame.display.update()

clock = pygame.time.Clock()
finished = False
balls = []

while not finished:
    clock.tick(FPS)
    for b in balls:
        b.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_ball = Ball(screen)
            balls.append(new_ball)
            if any(isCaught(event, b.get_x(), b.get_y(), b.get_r()) for b in balls):
                counter += 1

    text_surface = my_font.render(f'COUNTER: {counter}', False, (255, 255, 255))
    for b in balls:
        b.move()
        if b.hittest():
            b.fix_position()
            b.rand_v()

    pygame.display.update()
    screen.fill(BLACK)
    screen.blit(text_surface, (50, 50))

pygame.quit()