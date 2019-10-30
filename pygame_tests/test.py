#!/usr/bin/python3
import pygame

from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

speed = .1
x = 100
y = 100

screen = pygame.display.set_mode([500, 500])
running = True

while running:
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w]:
        y -= speed
    if pressed_keys[K_a]:
        x -= speed
    if pressed_keys[K_s]:
        y += speed
    if pressed_keys[K_d]:
        x += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 50)  
    pygame.display.flip()
pygame.quit()