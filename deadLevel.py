import pygame
from configs import *
from level import *
from level1 import *
from manager import *
from menu import *

# Level to represent that our player's health is less than 1
class FailLevel(Level):
    def __init__(self,director, level) :
        super().__init__(director)
        # We change the music to a specific sound for FailLevel
        mixer.music.unload()
        mixer.music.load('Music/ded.mp3')
        mixer.music.play(1)
        self.level = level
        # We change the background
        self.background = Manager.loadImage("sun.jpg")
        
    def update(self,time):
       mixer.music.unpause()

    def events(self,events):
        for event in events:
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    self.director.exitLevel()
                elif event.key == K_SPACE:
                    self.director.changeLevel(self.level)
            
    # We print the message and add a new image to the background
    def draw(self,screen):
        screen.fill(BLACK)
        screen.blit(self.background,[0,0])
        myfont=pygame.font.SysFont("Britannic Bold", 40)
        nlabel=myfont.render("You Are Dead, Son! Press Escape to return to the menu, or any other key to continue", 1, (255, 0, 0))
        screen.blit(nlabel,(100,200))