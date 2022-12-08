import pygame
import game_manager

pygame.init()

font = pygame.font.Font("assets/Oven Pixel Font.ttf", 12)
game = game_manager.GameManager()


if __name__ == '__main__':
    while True:
        game.display_current()
