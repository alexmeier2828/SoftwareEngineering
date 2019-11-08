import pygame
class EquationSquareView:
    def __init__(self, height, width, x, y , eq):
        #size
        self.h = height
        self.w = width
        #position
        self.x = x
        self.y = y
        #equation string
        self.equation = eq

    def draw(self, display):
        color = (200,200,200) # this should probably be defined in some style document
        pygame.draw.rect(display, color, (self.x, self.y, self.width, self.height))
        display.screen.blit(pygame.font.SysFont('Arial', 25).render(self.equation, True, (0,0,0)), (self.width, self.height))


        
