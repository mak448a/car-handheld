import pygame


pygame.init()

font = pygame.font.Font("assets/Oven Pixel Font.ttf", 8)


class Button:
    def __init__(self, text: str, pos: tuple, width: int, height: int):
        """A button class used for making menus."""
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
    def draw(self, surf: pygame.Surface):
        rect = pygame.Rect(self.pos, (self.width, self.height))
        pygame.draw.rect(surf, "blue", rect)
        text = font.render(self.text, False, "black")
        text_rect = text.get_rect()
        text_rect.centerx = rect.centerx
        text_rect.centery = rect.centery
        surf.blit(text, text_rect)
