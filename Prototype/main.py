#!/usr/bin/env python3

import pygame
from rectangle import EquationRect, new_easy_rectangle_pair
from menu import Menu
from style import Colors
from util import shuffle

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

BLOCK_SIZE = 100


def drawScoreAndTime():
    score_rect = pygame.Rect(0, 0, 90, 90)
    font = pygame.font.SysFont('Arial', 15)
    pygame.draw.rect(screen, Colors.GREY, score_rect, 1)
    screen.blit(font.render("00:00", True, Colors.WHITE), (score_rect.x + 5, score_rect.y + 10))
    screen.blit(font.render("Score: 0000", True, Colors.WHITE), (score_rect.x + 5, score_rect.y + 50))

def test_buckets():
    buckets = [pygame.Rect(100, 100, 150, 100), pygame.Rect(300, 100, 150, 100), pygame.Rect(500, 100, 150, 100)]
    answers = [pygame.Rect(100, 450, 150, 100), pygame.Rect(300, 450, 150, 100), pygame.Rect(500, 450, 150, 100)]
    shuffle(buckets)
    shuffle(answers)

    print(buckets)

    rects = []

    for i in range(0, len(buckets)):
        new_pair = new_easy_rectangle_pair(buckets[i], answers[i])
        rects.append(new_pair[0])
        rects.append(new_pair[1])


def run():
    selected = None

    clock = pygame.time.Clock()
    is_running = True
    show_menu = False
    game_finished = False;

    while is_running:

        #event handling
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
                        if r.collidepoint(event.pos) and grabbable and not show_menu:
                            selected = i
                            selected_offset_x = r.x - event.pos[0]
                            selected_offset_y = r.y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if selected is not None:
                        for r in playfield.buckets:
                            if r.rect.colliderect(rects[selected].rect) and r is not rects[selected] and rects[selected].value == r.value:
                                del rects[selected]
                                rects.remove(r)
                                break
                        selected = None

            elif event.type == pygame.MOUSEMOTION:
                if selected is not None: # selected can be `0` so `is not None` is required
                    # move object
                    rects[selected].rect.x = event.pos[0] + selected_offset_x
                    rects[selected].rect.y = event.pos[1] + selected_offset_y

        #keep track of game state here
        if len(rects) == 0:
            game_finished = True

        #draw graphics
        screen.fill(BLACK)
        hand = pygame.Rect(0, 400, 800, 200)
        pygame.draw.rect(screen, (100, 100, 100), hand)

        drawScoreAndTime()
        if game_finished:
            font = pygame.font.SysFont('Arial', 40)
            screen.blit(font.render("You Win!", True, Colors.WHITE), (300, 150))
        else:
            for r in rects:
                r.draw_on(screen)
            if show_menu:
                Menu.draw(screen)
        pygame.display.update()

        clock.tick(25)

    pygame.quit()

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()

    run()
