import pygame 
from pygame.locals import *
from configs import *
from sprites import *
from manager import *

# Class from which others inherit
class Sprit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.scroll = (0, 0)
