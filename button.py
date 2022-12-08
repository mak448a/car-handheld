import pygame


pygame.init()

font = pygame.font.Font("assets/Oven Pixel Font.ttf", 8)


class Button:
    def __init__(self, text: str, pos: tuple, width: int, height: int, color, game):
        """A button class used for making menus."""
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos, (self.width, self.height))
        self.color = color
        self.game = game
    def draw(self, surf: pygame.Surface):
        pygame.draw.rect(surf, "blue", self.rect)
        text = font.render(self.text, False, "black")
        text_rect = text.get_rect()
        text_rect.centerx = self.rect.centerx
        text_rect.centery = self.rect.centery
        surf.blit(text, text_rect)

    def check_collisions(self, pressed):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pressed:
            return True
