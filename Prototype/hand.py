import pygame
import copy

one = [pygame.Rect(300, 450, 150, 100)]

two = [pygame.Rect(200, 450, 150, 100), pygame.Rect(450, 450, 150, 100)]

three = [pygame.Rect(100, 450, 150, 100), pygame.Rect(325, 450, 150, 100), pygame.Rect(550, 450, 150, 100)]

four = [pygame.Rect(50, 450, 150, 100), pygame.Rect(233, 450, 150, 100), pygame.Rect(417, 450, 150, 100), pygame.Rect(600, 450, 150, 100)]

five = [pygame.Rect(175, 425, 100, 67), pygame.Rect(350, 425, 100, 67), pygame.Rect(525, 425, 100, 67), pygame.Rect(250, 510, 100, 67), pygame.Rect(450, 510, 100, 67)]

six = [pygame.Rect(175, 425, 100, 67), pygame.Rect(350, 425, 100, 67), pygame.Rect(525, 425, 100, 67), pygame.Rect(175, 510, 100, 67), pygame.Rect(350, 510, 100, 67), pygame.Rect(525, 510, 100, 67)]

seven = [pygame.Rect(125, 425, 100, 67), pygame.Rect(275, 425, 100, 67), pygame.Rect(425, 425, 100, 67), pygame.Rect(575, 425, 100, 67), pygame.Rect(175, 510, 100, 67), pygame.Rect(350, 510, 100, 67), pygame.Rect(525, 510, 100, 67)]

class Hand:
    def __init__(self):
        self.pieces = []
        self.extras = []
        self.overflow = False
    
    def add(self, rect):
        if len(self.pieces) < 7:
            self.pieces.append(rect)
        else: 
            self.extras.append(rect)
        self.realign()

    def remove(self, n):
        self.pieces.pop(n)
        if len(self.pieces) < 7 and len(self.extras) > 0:
            self.pieces.append(self.extras.pop(0))
        self.realign()

    def realign(self):
        rectangles = []
        if len(self.pieces) == 1:
            self.overflow = False
            rectangles = one
        elif len(self.pieces) == 2:
            self.overflow = False
            rectangles = two
        elif len(self.pieces) == 3:
            self.overflow = False
            rectangles = three
        elif len(self.pieces) == 4:
            self.overflow = False
            rectangles = four
        elif len(self.pieces) == 5:
            self.overflow = False
            rectangles = five
        elif len(self.pieces) == 6:
            self.overflow = False
            rectangles = six
        elif len(self.pieces) >= 7:
            rectangles = seven
            self.overflow = True

        for i in range(0, len(rectangles)):
            self.pieces[i].rect = copy.deepcopy(rectangles[i])