import pygame
from button import Button

pygame.init()
width, height = 200, 100
display = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.set_caption("Handheld Car Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    display.fill("grey")
    Button("Test", (2, 2), 30, 15).draw(display)
    pygame.display.update()
