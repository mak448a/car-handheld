import pygame

pygame.init()


def load_image(path):
    return pygame.image.load(path).convert_alpha()
