import pygame
from button import Button

pygame.init()
font = pygame.font.Font("assets/Oven Pixel Font.ttf", 20)

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = [
            Button("Play!", (20, 60), 30, 15, "blue", game),
            Button("Quit", (150, 60), 30, 15, "blue", game)
        ]
        self.bg = pygame.image.load("assets/title.png").convert()
        self.text = font.render("Car Handheld", False, "black")
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx, self.text_rect.centery = game.display.get_rect().centerx, game.display.get_rect().centery - 5
    def main_loop(self):
        while True:
            # Reset click variable
            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # User clicked mouse
                        click = True

            self.game.display.blit(self.bg, (0, 0))
            for button in self.buttons:
                button.draw(self.game.display)
                if button.check_collisions(click) and button.text == "Play!":
                    self.game.menu = "main_game"
                    return

            self.game.display.blit(self.text, self.text_rect)

            pygame.display.update()
