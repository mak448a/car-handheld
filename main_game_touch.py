import pygame
from game.enemy import Enemy
from game.player import Player
from game.road import Road
from button import Button
import random
import sys

pygame.init()
font = pygame.font.Font("assets/Oven Pixel Font.ttf", 12)
clock = pygame.time.Clock()
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 800)

def main_game(display, game):
    player = Player(display)
    enemies = pygame.sprite.Group()
    road = Road(display)
    buttons = [
        Button("<-", (10, 80), 15, 15, "blue", display),
        Button("->", (175, 80), 15, 15, "blue", display)
    ]
    # Get rid of extra cars that were added
    pygame.event.get()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == ADD_ENEMY:
                enemies.add(Enemy(display, game, random.choice(["m", "l", "r"])))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

        keys = pygame.key.get_pressed()
        player.update(keys)
        enemies.update()
        road.update()


        road.draw()
        enemies.draw(display)
        player.draw()

        score_text = font.render(str(game.score), False, "black")
        display.blit(score_text, (8, 4))

        for button in buttons:
            button.draw(display)
            if button.check_collisions(True):
                if button.text == "->":
                    player.rect.x += 4
                elif button.text == "<-":
                    player.rect.x -= 4

        pygame.display.update()

        for i, enemy in enumerate(enemies):
            if player.collide(enemy.mask, enemy.rect.x, enemy.rect.y):
                # Play a crash sound
                pygame.mixer.Sound("assets/crash.wav").play()
                game.menu = "crash_menu"
                game.score = 0
                return

        clock.tick(30)
