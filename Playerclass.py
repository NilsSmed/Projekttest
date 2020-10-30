import pygame
import os


ALPHA = (255, 0, 0)
animation = 3
animation_attack = 3


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_fwd = []
        self.images_fwd_attack = []

        self.images_rvs = []
        self.images_rvs_attack = []

        self.images_right = []
        self.images_right_attack = []

        self.images_left = []
        self.images_left_attack = []

        self.move_up = 0
        self.move_down = 0
        self.move_right = 0
        self.move_left = 0

        self.attack_left = 0
        self.attack_right = 0
        self.attack_fwd = 0
        self.attack_rvs = 0


        self.frame = 0

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_fwd" + str(i) + ".gif"))  #Comprahension?
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_fwd.append(img)
            self.image = self.images_fwd[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_rvs" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_rvs.append(img)
            self.image = self.images_rvs[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_right" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_right.append(img)
            self.image = self.images_right[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_left" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_left.append(img)
            self.image = self.images_left[0]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_left_attack" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_left_attack.append(img)
            self.image = self.images_left_attack[0]
            self.rect = self.image.get_rect()

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_right_attack" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_right_attack.append(img)
            self.image = self.images_right_attack[0]
            self.rect = self.image.get_rect()

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_fwd_attack" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_fwd_attack.append(img)
            self.image = self.images_fwd_attack[0]
            self.rect = self.image.get_rect()

        for i in range(1, 5):
            img = pygame.image.load(os.path.join("images", "Hero_rvs_attack" + str(i) + ".gif"))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images_rvs_attack.append(img)
            self.image = self.images_rvs_attack[0]
            self.rect = self.image.get_rect()

    def control(self, x, y, attack_left, attack_right, attack_fwd, attack_rvs):
        self.move_up += y
        self.rect.y -= self.move_up
        self.move_down -= y
        self.rect.y += self.move_down
        self.move_right -= x
        self.rect.x += self.move_right
        self.move_left += x
        self.rect.x -= self.move_left
        self.attack_left = self.attack_left
        self.attack_right = self.attack_right
        self.attack_fwd = self.attack_fwd
        self.attack_rvs = self.attack_rvs

        if self.attack_left is True:
            self.frame += 1
            if self.frame > 3*animation_attack:
                self.frame = 0
            self.image = self.images_left_attack[self.frame//animation_attack]
        self.attack_left = attack_left

        if self.attack_right is True:
            self.frame += 1
            if self.frame > 3*animation_attack:
                self.frame = 0
            self.image = self.images_right_attack[self.frame//animation_attack]
        self.attack_right = attack_right

        if self.attack_fwd is True:
            self.frame += 1
            if self.frame > 3*animation_attack:
                self.frame = 0
            self.image = self.images_fwd_attack[self.frame//animation_attack]
        self.attack_fwd = attack_fwd

        if self.attack_rvs is True:
            self.frame += 1
            if self.frame > 3*animation_attack:
                self.frame = 0
            self.image = self.images_rvs_attack[self.frame//animation_attack]
        self.attack_rvs = attack_rvs

        if self.move_up > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_fwd[self.frame//animation]
        self.move_up -= y  # använder denna två gånger? samma sak med move_down.
        self.rect.y -= self.move_up

        if self.move_down > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_rvs[self.frame//animation]
        self.move_down += y
        self.rect.y += self.move_down

        if self.move_right > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_right[self.frame//animation]
        self.move_right += x
        self.rect.x += self.move_right

        if self.move_left > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images_left[self.frame//animation]
        self.move_left -= x
        self.rect.x -= self.move_left

