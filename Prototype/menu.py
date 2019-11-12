import pygame
from style import Colors

class MenuButton:
    def __init__(self, pygame_rect, color, string):
        self.rect = pygame_rect
        self.string = string
        self.color = color

    def draw(self, screen):
        font = pygame.font.SysFont('Arial', 20)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(font.render(self.string, True, Colors.BLACK), (self.rect.x, self.rect.y ) )


class Menu:
    menu_rect = pygame.Rect(250, 100, 300, 300)
    border_rect = pygame.Rect(249, 99, 302, 302)
    easy = MenuButton(pygame.Rect(menu_rect.x + 50, menu_rect.y + 200, 50, 50), Colors.GREEN, "Easy")
    hard = MenuButton(pygame.Rect(menu_rect.x + 150, menu_rect.y + 200, 50, 50), Colors.RED, "Hard")

    def draw(screen):
        font = pygame.font.SysFont('Arial', 20)
        pygame.draw.rect(screen, Colors.GREY, Menu.border_rect) #This is kindof gross but its the only way I could find to get fileld rectangle with a border
        pygame.draw.rect(screen, Colors.BLACK, Menu.menu_rect)
        screen.blit(font.render("Select Dificulty:", True, Colors.WHITE), (Menu.menu_rect.x + 100, Menu.menu_rect.y + 20))
        Menu.easy.draw(screen)
        Menu.hard.draw(screen)
