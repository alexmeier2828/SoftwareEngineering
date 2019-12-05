import pygame
from rectangle import new_easy_rectangle_pair
from random import randint

COL_WIDTH = 200
COL_1_X = 150
COL_2_X = 350
COL_3_X = 550


class PlayField:
    def __init__(self):
        self.c1 = []
        self.c2 = []
        self.c3 = []

    def remove(self, n):
        removed = None

        if n > len(self.c1):
            n -= len(self.c1)
        else:
            removed = self.c1.pop(n)
            delta_y = removed.rect.height
            for i in range(n, len(self.c1)):
                self.c1[i].y -= delta_y
            return 0

        if n > len(self.c2):
            n -= len(self.c2)
        else:
            removed = self.c2.pop(n)
            delta_y = removed.rect.height
            for i in range(n, len(self.c2)):
                self.c2[i].y -= delta_y
            return 0
        
        removed = self.c3.pop(n)
        delta_y = removed.rect.height
        for i in range(n, len(self.c3)):
            self.c3[i].y -= delta_y
        return 0
        
    def buckets(self):
        l = []
        l.append(self.c1)
        l.append(self.c2)
        l.append(self.c3)
        return l

    def advance(self, hand):
        for b in self.c1:
            b.rect.y += 1
        for b in self.c2:
            b.rect.y += 1
        for b in self.c3:
            b.rect.y += 1
        if self.c1[0].rect.y > 0: 
            h = randint(25, 100)
            b, p = new_easy_rectangle_pair(pygame.Rect(COL_1_X, self.c1[0].rect.y - h, COL_WIDTH, h), )
        

class Hand:
    def __init__(self):
        self.pieces = []
    
    def add(self, rect):
        self.pieces.append(rect)

    def advance(self):
        pass