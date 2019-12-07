import pygame
from menu import MenuButton
from style import Colors

class GameOverScreen:
    go_rect = pygame.Rect(250, 100, 300, 300)
    border_rect = pygame.Rect(249, 99, 302, 302)
    restart = MenuButton(pygame.Rect(border_rect.x + 120, border_rect.y + 200, 60, 30), Colors.GREEN, "Restart")


    def draw(screen):
        font = pygame.font.SysFont('Arial', 20)
        pygame.draw.rect(screen, Colors.GREY, GameOverScreen.border_rect) #This is kindof gross but its the only way I could find to get fileld rectangle with a border
        pygame.draw.rect(screen, Colors.BLACK, GameOverScreen.go_rect)
        screen.blit(font.render("Game Over.", True, Colors.WHITE), (GameOverScreen.go_rect.x + 100, GameOverScreen.go_rect.y + 20))
        GameOverScreen.restart.draw(screen)
