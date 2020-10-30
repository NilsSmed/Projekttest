import pygame
import os
import random


ALPHA = (255, 0, 0)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.image_monster = pygame.image.load(os.path.join("images", "monster.png"))
        self.image_monster.convert_alpha()
        self.image_monster.set_colorkey(ALPHA)
        self.image = self.image_monster
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.mask = pygame.mask.from_surface(self.image)


    def movement(self):

        distance = random.randint(5, 15)
        speedx = random.randint(-10, 10)
        enemy1.rect.move_ip(-10, 0)
        #  enemy1.rect.move_ip(direction_x, direction_y)

    #irection_x = random.randint(-5, 5)
    #direction_y = random.randint(-5, 5)
    #enemy1.rect.move_ip(direction_x, direction_y)
    #directionclock = int()

    #if pygame.sprite.spritecollideany(enemy1, walls_list, pygame.sprite.collide_mask):
     #   enemy1.rect.move_ip(-10, 0)
      #  enemy1.rect.move_ip(direction_x, direction_y)


