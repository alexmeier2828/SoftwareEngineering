import pygame
from random import seed
from random import randint
from datetime import datetime

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

colors = [RED, GREEN, BLUE]

seed(datetime.now())

easy_equations = {}
easy_equations[0] = ["3 - 3", "0"]
easy_equations[1] = ["1", "0 + 1", "3 - 2", "5 - 4"]
easy_equations[2] = ["2", "1 + 1", "2 + 0", "3 - 1", "5 - 3"]
easy_equations[3] = ["3", "2 + 1", "1 + 2", "1 + 1 + 1", "5 - 2", "7 - 4"]
easy_equations[4] = ["4", "2 + 2", "3 + 1", "5 - 1", "7 - 3", "2 + 1 + 1"]
easy_equations[5] = ["5", "2 + 3", "4 + 1", "6 - 1", "8 - 3", "2 + 2 +1"]
easy_equations[6] = ["6", "3 + 3", "4 + 2", "5 + 1", "8 - 2", "10 - 4"]
easy_equations[7] = ["7", "4 + 3", "5 + 2", "6 + 1", "8 - 1", "14 - 7"]
easy_equations[8] = ["8", "4 + 4", "3 + 5", "6 + 2", "1 + 7", "10 - 2", "11 - 3"]
easy_equations[9] = ["9", "4 + 5", "3 + 6", "7 + 2", "10 - 1", "12 - 3"]
easy_equations[10] = ["10", "5 + 5", "4 + 6", "7 + 3", "15 - 5", "12 - 2"]


class EquationRect:
    def __init__(self, pygame_rect, color, equation, value, grabbable):
        self.rect = pygame_rect
        self.equation = equation
        self.color = color
        self.value = value
        self.grabbable = grabbable

    def draw_on(self, screen):
        font = pygame.font.SysFont('Arial', 32)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(font.render(self.equation, True, BLACK), (self.rect.x, self.rect.y ) )


def new_easy_rectangle_pair(r1, r2):
    val = randint(0, 10)
    bucket = EquationRect(r1, RED, easy_equations[val][randint(0, len(easy_equations[val]) - 1)], val, False)
    rect = EquationRect(r2, BLUE, easy_equations[val][randint(0, len(easy_equations[val]) - 1)], val, True)
    return (bucket, rect)
