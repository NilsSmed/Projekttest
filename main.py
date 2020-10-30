import pygame
import os
import random
from Playerclass import Player
from Enemyclass import Enemy
from World import Walls


SCR_WIDTH = 1600
SCR_HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ALPHA = (255, 0, 0)
fps = 30
animation = 9
screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])


def main():
    pygame.init()
    background = pygame.image.load(os.path.join("images", "background.jpg"))
    background = pygame.transform.scale(background, (SCR_WIDTH, SCR_HEIGHT))
    clock = pygame.time.Clock()
    bgbox = screen.get_rect()
    player = Player()

    enemy1 = Enemy(512, 300)
    enemy2 = Enemy(0, 0)

    walls = Walls(0, 0)

    player.rect.x = 1400
    player.rect.y = 180

    enemy1.rect.x = 512
    enemy1.rect.y = 300
    enemy2.rect.x = 1400
    enemy2.rect.y = 100

    walls.rect.x = 0
    walls.rect.y = 0

    player_list = pygame.sprite.Group()
    player_list.add(player)

    enemy_list = pygame.sprite.Group()
    enemy_list.add(enemy1, enemy2)

    walls_list = pygame.sprite.Group()
    walls_list.add(walls)

    steps_x = 2
    steps_y = 2

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button_pressed = pygame.key.get_pressed()  # lägg till i player-classen?
        if button_pressed[pygame.K_w] and not button_pressed[pygame.K_SPACE]:
            player.rect.y -= 1
            player.control(0, steps_y, 0, 0, 0, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.y += 5
            if pygame.sprite.groupcollide(player_list, enemy_list, True, False, pygame.sprite.collide_mask):
                print("Dead")
        if button_pressed[pygame.K_s] and not button_pressed[pygame.K_SPACE]:
            player.rect.y += 1
            player.control(0, -steps_y, 0, 0, 0, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.y -= 5
            if pygame.sprite.groupcollide(player_list, enemy_list, True, False, pygame.sprite.collide_mask):
                print("Dead")
        if button_pressed[pygame.K_d] and not button_pressed[pygame.K_SPACE]:
            player.rect.x += 1
            player.control(-steps_x, 0, 0, 0, 0, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.x -= 5
            if pygame.sprite.groupcollide(player_list, enemy_list, True, False, pygame.sprite.collide_mask):
                print("Dead")
        if button_pressed[pygame.K_a] and not button_pressed[pygame.K_SPACE]:
            player.rect.x -= 1
            player.control(steps_x, 0, 0, 0, 0, 0)
            if pygame.sprite.spritecollideany(player, walls_list, pygame.sprite.collide_mask):
                player.rect.x += 5
            if pygame.sprite.groupcollide(player_list, enemy_list, True, False, pygame.sprite.collide_mask):
                print("Dead")
        if button_pressed[pygame.K_SPACE] and button_pressed[pygame.K_a]:
            player.control(0, 0, True, 0, 0, 0)
            if pygame.sprite.spritecollide(sprite=player, dokill=True, group=enemy_list):
                print("Collide")
        if button_pressed[pygame.K_SPACE] and button_pressed[pygame.K_d]:
            player.control(0, 0, 0, True, 0, 0)
            if pygame.sprite.spritecollide(sprite=player, dokill=True, group=enemy_list):
                print("Collide")
        if button_pressed[pygame.K_SPACE] and button_pressed[pygame.K_w]:
            player.control(0, 0, 0, 0, True, 0)
            if pygame.sprite.spritecollide(sprite=player, dokill=True, group=enemy_list):
                print("Collide")
        if button_pressed[pygame.K_SPACE] and button_pressed[pygame.K_s]:
            player.control(0, 0, 0, 0, 0, True)
            if pygame.sprite.spritecollide(sprite=player, dokill=True, group=enemy_list):
                print("Collide")


        walls_list.update()
        walls_list.draw(screen)

        screen.blit(background, bgbox)

        player_list.update()
        player_list.draw(screen)

        enemy_list.update()
        enemy_list.draw(screen)

        pygame.display.update()
        clock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
