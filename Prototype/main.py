#!/usr/bin/env python3

import pygame
import time
from playfield import PlayField
from hand import Hand
from rectangle import EquationRect, new_easy_rectangle_pair
from menu import Menu
from gameOverScreen import GameOverScreen
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

WINDOW_TITLE = "MathMatch"

HAND_AREA = pygame.Rect(0, 400, 800, 200)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE) #sets window title.
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
    global game_finished
    global startTime
    global scoreKeeper
    hard = False

    playfield = PlayField()
    hand = Hand()


    clock = pygame.time.Clock()
    is_running = True
    show_menu = True

    while is_running:
        if not show_menu:
            playfield.advance(hand, hard)
            clock.tick(25)

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
                        hard = False
                        show_menu = False
                    if show_menu and Menu.hard.rect.collidepoint(event.pos):
                        hard = True
                        show_menu = False

                    #catch event for GameOverScreen
                    if game_finished and GameOverScreen.restart.rect.collidepoint(event.pos):
                        game_finished = False
                        show_menu = False           #set this to true when select dificulty is a thing
                        scoreKeeper = ScoreKeeper()
                        playfield = PlayField()
                        hand = Hand()
                        startTime = time.time();
                        elapsedTime = 0


                    for i, r in enumerate(hand.pieces):
                        grabbable = r.grabbable
                        r = r.rect
                        if r.collidepoint(event.pos) and grabbable and not show_menu:
                            hand.selected = i
                            selected_offset_x = r.x - event.pos[0]
                            selected_offset_y = r.y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if hand.selected is not None:
                        buckets = playfield.buckets()
                        foundMatch = False
                        for i in range(0, len(buckets)):
                            if buckets[i].rect.colliderect(hand.selected_piece().rect) and buckets[i].value == hand.selected_piece().value:
                                playfield.remove(i)
                                hand.remove(hand.selected)
                                scoreKeeper.increment(buckets[i].value) #increment score by 10
                                foundMatch = True
                                break

                        #reset combo if no matching piece was selected
                        if foundMatch == False:
                            scoreKeeper.endCombo()
                        hand.selected = None
                        hand.realign()

            elif event.type == pygame.MOUSEMOTION:
                if hand.selected is not None: # selected can be `0` so `is not None` is required
                    # move object
                    hand.selected_piece().rect.x = event.pos[0] + selected_offset_x
                    hand.selected_piece().rect.y = event.pos[1] + selected_offset_y

        #keep track of game state here
        buckets = playfield.buckets()
        for bucket in buckets:
            if bucket.rect.colliderect(HAND_AREA):
                game_finished = True                #game over condition


        #draw graphics
        screen.fill(BLACK)
        pygame.draw.rect(screen, (100, 100, 100), HAND_AREA)

        drawScoreAndTime()
        if game_finished:
            GameOverScreen.draw(screen)
        else:
            for r in playfield.buckets():
                r.draw_on(screen)
            for r in hand.pieces:
                r.draw_on(screen)
            if show_menu:
                Menu.draw(screen)
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    run()
