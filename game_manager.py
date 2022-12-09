import pygame
from main_game import main_game
from main_menu import MainMenu
from crash_menu import CrashMenu
from utils import load_image

pygame.init()

class GameManager:
    def __init__(self):
        self.score = 0
        self.width, self.height = 200, 100
        self.display = pygame.display.set_mode((self.width, self.height), pygame.SCALED)
        pygame.display.set_caption("Handheld Car Game")
        pygame.display.set_icon(load_image("assets/icon.png"))

        self.main_menu = MainMenu(self)
        self.crash_menu = CrashMenu(self)
        self.menu = "main_menu"

    def main_loop(self):
        main_game(self.display, self)

    def display_current(self):
        if self.menu == "main_menu":
            self.main_menu.main_loop()
        elif self.menu == "main_game":
            self.main_loop()
        elif self.menu == "crash_menu":
            self.crash_menu.main_loop()
