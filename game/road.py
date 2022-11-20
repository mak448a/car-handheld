from utils import load_image
import pygame


pygame.init()


class Road:
    def __init__(self, display):
        self.images = [
            load_image("road1.png"),
            load_image("road2.png")
        ]
        self.display = display
        self.iter = 0
        self.image = self.images[self.iter]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        self.display.blit(self.image, self.rect)

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        # Helped along with this article
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
        if self.iter + 1 >= len(self.images) * 3:
            self.iter = 0
            return

        self.image = self.images[self.iter // 3]

        self.iter += 1
