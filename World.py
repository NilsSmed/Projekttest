import pygame
import os

ALPHA = (255, 0, 0)


class Walls(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.image_walls = pygame.image.load(os.path.join("images", "walls.png"))
        self.image_walls.convert_alpha()
        self.image_walls.set_colorkey(ALPHA)
        self.image = self.image_walls
        self.rect = self.image.get_rect()
        self.rect_x = x
        self.rect_y = y
        self.mask = pygame.mask.from_surface(self.image)


