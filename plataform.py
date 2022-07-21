import pygame
from pygame.locals import *
from manager import *
from sprite import Sprit

# Class to create all the elements we can collide with 
class Plataform(Sprit):
    def __init__(self,rect, image, level):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        # Empty to represent the base level, the ground
        if(image == "empty"):
            aux_image = pygame.Surface((0, 0)).convert_alpha()
        else:
            # Anything else: cars, columns, platforms, etc
            aux_image = Manager.loadImage(image).convert_alpha()
        self.image = pygame.transform.scale(aux_image, (self.rect.width,self.rect.height))
        self.level = level

    def update(self, time):
        return
    
    def draw(self, screen):
        aux = self.level.camera.apply(self)
        screen.blit(self.image, aux)
