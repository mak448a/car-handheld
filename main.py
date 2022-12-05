import pygame
import game_manager
from game.enemy import Enemy
from game.player import Player
from game.road import Road
import random

pygame.init()

width, height = 200, 100
display = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.set_caption("Handheld Car Game")
pygame.display.set_icon(pygame.image.load("assets/icon.png").convert_alpha())
clock = pygame.time.Clock()


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 800)

font = pygame.font.Font("assets/Oven Pixel Font.ttf", 12)
game = game_manager.GameManager()

player = Player(display)
enemies = pygame.sprite.Group()
enemy = Enemy(display, game, "m")
enemies.add(enemy)
road = Road(display)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == ADDENEMY:
            enemies.add(Enemy(display, game, random.choice(["m", "l", "r"])))

    keys = pygame.key.get_pressed()
    player.update(keys)
    enemies.update()
    road.update()


    road.draw()
    enemies.draw(display)
    player.draw()

    score_text = font.render(str(game.score), False, "black")
    display.blit(score_text, (8, 4))

    pygame.display.update()

    for i, enemy in enumerate(enemies):
        if player.collide(enemy.mask, enemy.rect.x, enemy.rect.y):
            # Play a crash sound
            pygame.mixer.Sound("crash.wav").play()
            pygame.time.delay(500)
            quit()

    clock.tick(30)
