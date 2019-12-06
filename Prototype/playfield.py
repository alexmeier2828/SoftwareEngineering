import pygame
from rectangle import new_easy_rectangle_pair
from random import randint

HAND_REC = pygame.Rect(100, 100, 100, 100)
COL_WIDTH = 200
COL_1_X = 150
COL_2_X = 350
COL_3_X = 550


class PlayField:
    def __init__(self):
        self.progress = 0
        self.speed = .5
        self.c1 = []
        self.c2 = []
        self.c3 = []

    def remove(self, n):
        removed = None

        if n >= len(self.c1):
            n -= len(self.c1)
        else:
            removed = self.c1.pop(n)
            delta_y = removed.rect.height
            for i in range(n, len(self.c1)):
                self.c1[i].rect.y -= delta_y
            return 0

        if n >= len(self.c2):
            n -= len(self.c2)
        else:
            removed = self.c2.pop(n)
            delta_y = removed.rect.height
            for i in range(n, len(self.c2)):
                self.c2[i].rect.y -= delta_y
            return 0
        
        removed = self.c3.pop(n)
        delta_y = removed.rect.height
        for i in range(n, len(self.c3)):
            self.c3[i].rect.y -= delta_y
        return 0
        
    def buckets(self):
        return self.c1 + self.c2 + self.c3

    def advance(self, hand):
        self.progress += self.speed
        while self.progress > 1:
            self.progress -= 1
            for b in self.c1:
                b.rect.y += 1
            for b in self.c2:
                b.rect.y += 1
            for b in self.c3:
                b.rect.y += 1

        hand.shuffle += .01

        if len(self.c1) < 1:
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_1_X, -h, COL_WIDTH, h), HAND_REC)
            self.c1.append(b)
            hand.add(p)
        if self.c1[0].rect.y > 0.0: 
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_1_X, self.c1[0].rect.y - h, COL_WIDTH, h), HAND_REC)
            self.c1.insert(0, b)
            hand.add(p)
        if len(self.c2) < 1:
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_2_X, -h, COL_WIDTH, h), HAND_REC)
            self.c2.append(b)
            hand.add(p)
        if self.c2[0].rect.y > 0.0: 
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_2_X, self.c2[0].rect.y - h, COL_WIDTH, h), HAND_REC)
            self.c2.insert(0, b)
            hand.add(p)
        if len(self.c3) < 1:
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_3_X, -h, COL_WIDTH, h), HAND_REC)
            self.c3.append(b)
            hand.add(p)
        if self.c3[0].rect.y > 0.0: 
            h = 100
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_3_X, self.c3[0].rect.y - h, COL_WIDTH, h), HAND_REC)
            self.c3.insert(0, b)
            hand.add(p)
        
        
