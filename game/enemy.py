import pygame
from .car import Car
from utils import load_image

pygame.init()


class Enemy(Car):
    middle_points = [(100, 40), (100, 45), (100, 50), (100, 55), (100, 60), (100, 75), (100, 90)]
    left_points = [(93, 40), (90, 43), (87, 46), (81, 52), (75, 58), (61, 70), (31, 100)]
    right_points = [(106, 40), (109, 43), (112, 46), (118, 52), (124, 58), (138, 70), (168, 100)]

    def __init__(self, display, game, direction="m"):
        # Direction must be in this list ["m", "r", "l"]
        img = load_image("assets/enemy_car_passing.png")
        images = [
            pygame.transform.scale(img, (8 / 2, 8 / 2)),
            pygame.transform.scale(img, (8 / 1.5, 8 / 1.5)),
            pygame.transform.scale(img, (16 / 2, 16 / 2)),
            pygame.transform.scale(img, (16 / 1.5, 16 / 1.5)),
            pygame.transform.scale(img, (32 / 2.1, 32 / 2)),
            pygame.transform.scale(img, (32 / 1.4, 32 / 1.5)),
            img
        ]
        self.direction = direction
        self.game = game
        super(Enemy, self).__init__(images, display)

        if direction == "m":
            self.rect.y = 60
            self.rect.centerx = display.get_width() / 2
            self.path = self.middle_points
        elif direction == "r":
            self.path = self.right_points
            self.rect.y = 40
        elif direction == "l":
            self.path = self.left_points
            self.rect.y = 40
        else:
            raise Exception("You must pass a valid path for the enemy car.")

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        # Helped along with this article
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
        if self.iter + 1 >= len(self.images) * 4:
            self.iter = 0
            self.game.score += 1
            # Done with iterations, kill the object
            self.kill()
            return

        self.image = self.images[self.iter // 4]

        new_rect = self.image.get_rect()
        new_rect.x, new_rect.y = self.rect.x, self.rect.y
        self.rect = new_rect

        self.rect.center = self.path[self.iter // 4]

        self.iter += 1
