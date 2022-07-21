from player import *
from configs import *


class Level():
    def __init__(self,director) :
        self.director = director

    def update(self, *args):
        raise NotImplemented("Update method needs to be implemented.")

    def events(self, *args):
        raise NotImplemented("Events method needs to be implemented.")

    # Print our player's health
    def check_health(self, screen):
        heart = Manager.loadImageScaled("heart.png", 80, 80)
        heart = heart.convert_alpha()
       
        for i in range(self.player.health):
            screen.blit(heart, (50*i, 10))

    def draw(self, screen):
        self.check_health(screen)