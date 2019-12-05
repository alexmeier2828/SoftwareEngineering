#!/usr/bin/env python3

import pygame
import time
from playfield import PlayField
from hand import Hand
from rectangle import EquationRect, new_easy_rectangle_pair
from menu import Menu
from style import Colors
from util import shuffle
from random import randint
from scoreKeeper import ScoreKeeper

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

scoreKeeper = ScoreKeeper() #this should probably be in  the game class when that exists
startTime = time.time() #start timer
elapsedTime = time.time() - startTime

game_finished = False;

def drawScoreAndTime():
    global elapsedTime #this is not ideal but it works until we have a class to put everything in.
    score_rect = pygame.Rect(0, 0, 90, 90)
    font = pygame.font.SysFont('Arial', 15)
    pygame.draw.rect(screen, Colors.GREY, score_rect, 1)

    if(game_finished == False):
        elapsedTime = time.time() - startTime

    timeString = time.strftime("%M:%S", time.gmtime(elapsedTime));

    screen.blit(font.render("Time: " + timeString, True, Colors.WHITE), (score_rect.x + 5, score_rect.y + 10))
    screen.blit(font.render("Score: " +str(scoreKeeper.score), True, Colors.WHITE), (score_rect.x + 5, score_rect.y + 50))

def run():
    selected = None

    playfield = PlayField()
    hand = Hand()
    

    clock = pygame.time.Clock()
    is_running = True
    show_menu = False


    while is_running:
        playfield.advance(hand)
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                if event.key == pygame.K_a:
                    a,b = new_easy_rectangle_pair(pygame.Rect(100, 100, 100, 100), pygame.Rect(100, 100, 100, 100))
                    hand.add(b)
                if event.key == pygame.K_l:
                    to_remove = randint(0, len(hand.pieces) - 1)
                    hand.remove(to_remove)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    #catch event for dificulty selection
                    if show_menu and Menu.easy.rect.collidepoint(event.pos):
                        show_menu = False
                    if show_menu and Menu.hard.rect.collidepoint(event.pos):
                        show_menu = False

                    for i, r in enumerate(hand.pieces):
                        grabbable = r.grabbable
                        r = r.rect
                        if r.collidepoint(event.pos) and grabbable and not show_menu:
                            selected = i
                            selected_offset_x = r.x - event.pos[0]
                            selected_offset_y = r.y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if selected is not None:
                        buckets = playfield.buckets()
                        print("buckets:", buckets)
                        for i in range(0, len(buckets)):
                            print("checking ", i)
                            if buckets[i].rect.colliderect(hand.pieces[selected].rect) and buckets[i].value == hand.pieces[selected].value:
                                print("MATCH!!!! i = ", i)
                                playfield.remove(i)
                                hand.remove(selected)
                                scoreKeeper.increment(10) #increment score by 10
                            else:
                                scoreKeeper.endCombo()
                        selected = None
                        hand.realign()

            elif event.type == pygame.MOUSEMOTION:
                if selected is not None: # selected can be `0` so `is not None` is required
                    # move object
                    hand.pieces[selected].rect.x = event.pos[0] + selected_offset_x
                    hand.pieces[selected].rect.y = event.pos[1] + selected_offset_y

        #keep track of game state here
        # if len(rects) == 0:
        #    game_finished = True

        #draw graphics
        screen.fill(BLACK)
        hand_area = pygame.Rect(0, 400, 800, 200)
        pygame.draw.rect(screen, (100, 100, 100), hand_area)

        drawScoreAndTime()
        if game_finished:
            font = pygame.font.SysFont('Arial', 40)
            screen.blit(font.render("You Win!", True, Colors.WHITE), (300, 150))
        else:
            for r in playfield.buckets():
                r.draw_on(screen)
            for r in hand.pieces:
                r.draw_on(screen)
            if show_menu:
                Menu.draw(screen)
        pygame.display.update()

        clock.tick(25)

    pygame.quit()

if __name__ == '__main__':
    run()