import pygame
from .car import Car
from utils import load_image

pygame.init()


class Player(Car):
    def __init__(self, display):
        images = [load_image("assets/player_car.png")]
        super(Player, self).__init__(images, display)
        self.rect.y = 60
        self.rect.centerx = display.get_width() / 2

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4

        # Keep the car on the screen
        # Code snippet by Real Python
        # Modified to fit the needs of this game
        # Source:
        # https://github.com/realpython/pygame-primer/blob/master/py_tutfinal.py

        right_side = self.display.get_width() - 30
        left_side = 30
        if self.rect.right > right_side:
            self.rect.right = right_side
        if self.rect.left < left_side:
            self.rect.left = left_side

    def collide(self, mask, x=0, y=0):
        # Written by techwithtim edited slightly to fit this game, thanks!
        offset = (int(self.rect.x - x), int(self.rect.y - y))
        poi = mask.overlap(self.mask, offset)
        return poi
