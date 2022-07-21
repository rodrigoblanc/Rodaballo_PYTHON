import pygame 
from pygame.locals import *
from configs import *
from sprites import *
from manager import *
from sprite import *
from character import *


# Class to define our main character
class MainCharacter(Character):
    def __init__(self, position, level):
        super().__init__(position,level)
        self.sheet = Manager.loadImage(PLAYER)
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        # Default position: no movement + looking right 
        self.desired_direction = 'stand_right'
        # It's default health
        self.health = 10
        self.weapon = False
        
    # Check collisions with powerups
    def check_power_ups(self):
        for sprite in self.level.powerups.sprites():
            if sprite.rect.colliderect(self.rect):
                #Set the powerup as used
                sprite.used = True
    
    def update(self, direction, time):
        super().update(direction, time)
        self.check_power_ups()