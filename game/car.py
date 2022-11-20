import pygame

pygame.init()


class Car(pygame.sprite.Sprite):
    def __init__(self, images: list, display: pygame.Surface):
        super(Car, self).__init__()
        self.images = []
        self.display = display
        # IMPORTANT! YOU MUST LOAD THE IMAGE FIRST!
        for image in images:
            self.images.append(image)
        self.iter = 0
        self.image = self.images[self.iter]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        self.display.blit(self.image, self.rect)
