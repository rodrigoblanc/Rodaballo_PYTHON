import pygame
from configs import *
from manager import *
from menu import *

# Pause level that we can open while we're playing levels: 1, 2 or 3
class LevelMenu(Level):
    def __init__(self,director) :
        super().__init__(director)
        self.background = Manager.loadImage("controls.png")
        
    def update(self,time):
        pass

    def events(self,events):
        # Different options for different keys pressed
        for event in events:
            if event.type == QUIT:
                # Exit to main menu
                self.director.exitLevel()
                self.director.exitLevel()
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    # Exit to main menu
                    self.director.exitLevel()
                    self.director.exitLevel()
                else:
                    if event.key == K_r:
                        # Back to the game
                        mixer.music.unpause()
                        self.director.exitLevel()
                    
    def draw(self,screen):
        screen.fill(BLACK)
        screen.blit(self.background,[0,0])
        myfont=pygame.font.SysFont("Britannic Bold", 100)
        myfont2=pygame.font.SysFont("Britannic Bold", 60)
        nlabel=myfont.render("HAVE A REST", 1, (255, 0, 0))
        olabel=myfont2.render("PRESS ESC TO RETURN TO THE MENU", 1, (255, 0, 0))
        screen.blit(nlabel,(700,200))
        screen.blit(olabel,(300,550))