#!/usr/bin/env python3

import pygame
from menu import Menu
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

BLOCK_SIZE = 100

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

class EquationRect:
    def __init__(self, pygame_rect, color, equation, value, grabbable):
        self.rect = pygame_rect
        self.equation = equation
        self.color = color
        self.value = value
        self.grabbable = grabbable

    def draw(self):
        font = pygame.font.SysFont('Arial', 32)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(font.render(self.equation, True, BLACK), (self.rect.x, self.rect.y ) )

rects = []


rects.append( EquationRect(pygame.Rect(100, 100, 150, 100), RED, "1 + 3", 4, False) )
rects.append( EquationRect(pygame.Rect(300, 100, 150, 100), RED, "4 + 4", 8, False) )
rects.append( EquationRect(pygame.Rect(500, 100, 150, 100), RED, "10 / 2", 5, False) )

rects.append( EquationRect(pygame.Rect(500, 450, 150, 100), BLUE, "7 - 3", 4, True) )
rects.append( EquationRect(pygame.Rect(100, 450, 150, 100), BLUE, "6 + 2", 8, True) )
rects.append( EquationRect(pygame.Rect(300, 450, 150, 100), BLUE, "1 * 5", 5, True) )


selected = None

clock = pygame.time.Clock()
is_running = True
show_menu = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                #catch event for dificulty selection
                if show_menu and Menu.easy.rect.collidepoint(event.pos):
                    show_menu = False
                if show_menu and Menu.hard.rect.collidepoint(event.pos):
                    show_menu = False
                
                for i, r in enumerate(rects):
                    grabbable = r.grabbable
                    r = r.rect
                    if r.collidepoint(event.pos) and grabbable:
                        selected = i
                        selected_offset_x = r.x - event.pos[0]
                        selected_offset_y = r.y - event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if selected is not None:
                    for r in rects:
                        print(r.rect.colliderect(rects[selected].rect))
                        if r.rect.colliderect(rects[selected].rect) and r is not rects[selected] and rects[selected].value == r.value:
                            del rects[selected]
                            rects.remove(r)
                            break
                    print("-----------------")
                    selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None: # selected can be `0` so `is not None` is required
                # move object
                rects[selected].rect.x = event.pos[0] + selected_offset_x
                rects[selected].rect.y = event.pos[1] + selected_offset_y
    screen.fill(BLACK)
    hand = pygame.Rect(0, 400, 800, 200)
    pygame.draw.rect(screen, (100, 100, 100), hand)

    for r in rects:
        r.draw()
    if show_menu:
        Menu.draw(screen)
    pygame.display.update()

    clock.tick(25)

pygame.quit()
