import pygame
from random import seed
from random import randint
from datetime import datetime

BLACK = (40, 44, 52)
WHITE = (171, 178, 191)

PURPLE = (198, 120, 221)
GREEN  = (152, 195, 121)
ORANGE = (209, 154, 102)
BLUE   = ( 97, 175, 233)
RED    = (224, 108, 117)
GOLD   = (229, 192, 123)

colors = [RED, GREEN, ORANGE, GOLD, PURPLE]

seed(datetime.now())

easy_equations = {}
easy_equations[0] = ["0", "3 - 3", "1 - 1"]
easy_equations[1] = ["1", "0 + 1", "3 - 2", "5 - 4"]
easy_equations[2] = ["2", "1 + 1", "2 + 0", "3 - 1", "5 - 3"]
easy_equations[3] = ["3", "2 + 1", "1 + 2", "1 + 1", "5 - 2", "7 - 4"]
easy_equations[4] = ["4", "2 + 2", "3 + 1", "5 - 1", "7 - 3"]
easy_equations[5] = ["5", "2 + 3", "4 + 1", "6 - 1", "8 - 3"]
easy_equations[6] = ["6", "3 + 3", "4 + 2", "5 + 1", "8 - 2", "10 - 4"]
easy_equations[7] = ["7", "4 + 3", "5 + 2", "6 + 1", "8 - 1", "14 - 7"]
easy_equations[8] = ["8", "4 + 4", "3 + 5", "6 + 2", "1 + 7", "10 - 2", "11 - 3"]
easy_equations[9] = ["9", "4 + 5", "3 + 6", "7 + 2", "10 - 1", "12 - 3"]
easy_equations[10] = ["10", "5 + 5", "4 + 6", "7 + 3", "15 - 5", "12 - 2"]
easy_equations[11] = ["11", "5 + 6", "4 + 7", "10 + 1", "15 - 4", "8 + 3"]
easy_equations[12] = ["12", "5 + 7", "10 + 2", "8 + 4", "14 - 2", "1 + 11", "13 - 1"]
easy_equations[13] = ["13", "8 + 5", "10 + 3", "7 + 6", "15 - 2"]

hard_equations = {}
hard_equations[0] = ["0", "0 / 5", "12 * 0", "6 - 6"]
hard_equations[1] = ["1", "13 / 13", "5 / 5", "4 - 3", "1 * 1"]
hard_equations[2] = ["2", "2 * 1", "8 / 4", "4 / 2", "8 - 6"]
hard_equations[3] = ["3", "3 * 1", "9 / 3", "12 / 4", "2 + 1", "15 / 5"]
hard_equations[4] = ["4", "2 * 2", "4 * 1", "12 / 3", "8 / 2", "10 - 6"]
hard_equations[5] = ["5", "5 * 1", "10 / 2", "15 / 3", "10 - 5"]
hard_equations[6] = ["6", "3 * 2", "2 * 3", "1 * 6", "12 / 2", "10 - 4"]
hard_equations[7] = ["7", "1 * 7", "14 / 2", "10 - 3", "5 + 2"]
hard_equations[8] = ["8", "2 * 4", "16 / 2", "10 - 2"]
hard_equations[9] = ["9", "3 * 3", "9 * 1", "10 - 1", "5 + 4"]
hard_equations[10] = ["10", "5 * 2", "20 / 2", "5 + 5", "15 - 5", "2 * 5"]
hard_equations[11] = ["11", "1 * 11", "5 + 6", "4 + 7", "10 + 1", "15 - 4", "8 + 3"]
hard_equations[12] = ["12", "2 * 6", "3 * 4", "4 * 3", "1 * 12", "10 + 2"]
hard_equations[13] = ["13", "1 * 13", "13 * 1", "10 + 3", "7 + 6", "15 - 2"]

class EquationRect:
    def __init__(self, pygame_rect, color, equation, value, grabbable):
        self.rect = pygame_rect
        self.equation = equation
        self.color = color
        self.value = value
        self.grabbable = grabbable

    def draw_on(self, screen):
        if self.rect.width > 110:
            font = pygame.font.SysFont('Ubuntu Mono', 32)
        else:
            font = pygame.font.SysFont('Ubuntu Mono', 24)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(font.render(self.equation, True, BLACK), (self.rect.x + 10, self.rect.y + self.rect.height * 0.5) )

def new_rectangle_pair(hard, r1, r2):
    if hard:
        return new_hard_rectangle_pair(r1, r2)
    else: 
        return new_easy_rectangle_pair(r1, r2)

def new_easy_rectangle_pair(r1, r2):
    val = randint(0, 13)
    color = randint(0, 4)
    bucket = EquationRect(r1, colors[color], easy_equations[val][randint(0, len(easy_equations[val]) - 1)], val, False)
    rect = EquationRect(r2, BLUE, easy_equations[val][randint(0, len(easy_equations[val]) - 1)], val, True)
    return (bucket, rect)

def new_hard_rectangle_pair(r1, r2):
    val = randint(0, 13)
    color = randint(0, 4)
    bucket = EquationRect(r1, colors[color], hard_equations[val][randint(0, len(hard_equations[val]) - 1)], val, False)
    rect = EquationRect(r2, BLUE, hard_equations[val][randint(0, len(hard_equations[val]) - 1)], val, True)
    return (bucket, rect)

