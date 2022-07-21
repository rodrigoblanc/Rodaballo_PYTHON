import pygame
from configs import *
from manager import *
from menu import *

# Level that we can reach if the kill the bosses from levels 1 and 2
class LevelPass(Level):
    def __init__(self,director, level, auxVolume) :
        super().__init__(director)
        # Each level will have its own song and volume
        self.auxVolume = auxVolume
        mixer.music.unload()
        mixer.music.load('Music/jalisia.mp3')
        pygame.mixer.music.set_volume(self.auxVolume)
        mixer.music.play(-1)
        self.level = level
        self.background = Manager.loadImage("CARALLO.png")
        
    def update(self,time):
        # Check if the music stream is playing
       if not(mixer.music.get_busy()):
           # If not, play this level's song
            mixer.music.load('Music/jalisia.mp3')
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)

    def events(self,events):
        # Different options for different keys pressed: ESCAPE, SPACE
        for event in events:
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    # Exit to main menu
                    mixer.music.pause()
                    self.director.exitLevel()
                elif event.key == K_SPACE:
                    # Pass to the next level
                    mixer.music.unload()
                    self.director.changeLevel(self.level)
                    
    def draw(self,screen):
        screen.fill(BLACK)
        screen.blit(self.background,[0,0])
        myfont=pygame.font.SysFont("Britannic Bold", 100)
        nlabel=myfont.render("CONGRATS, LEVEL CLEARED!", 1, (255, 0, 0))
        screen.blit(nlabel,(250,200))
        olabel=myfont.render("PRESS SPACE TO CONTINUE", 1, (255, 0, 0))
        screen.blit(olabel,(250,500))

# Level that we can reach if the kill the boss from levels 3
class GameCompleted(Level):
    def __init__(self,director, auxVolume) :
        super().__init__(director)
        # Each level will have its own song and volume
        self.auxVolume = auxVolume
        mixer.music.unload()
        mixer.music.load('Music/jalisia.mp3')
        pygame.mixer.music.set_volume(self.auxVolume)
        mixer.music.play(-1)
        self.background = Manager.loadImage("youwinner.jpg")
        
    def update(self,time):
        # Check if the music stream is playing
       if not(mixer.music.get_busy()):
           # If not, play this level's song
            mixer.music.load('Music/jalisia.mp3')
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)

    def events(self,events):
        # Different options for different keys pressed: ESCAPE, SPACE, RETURN
        for event in events:
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    # Exit to main menu
                    mixer.music.pause()
                    self.director.exitLevel()
                elif event.key == K_SPACE:
                    # Exit to main menu
                    mixer.music.unload()
                    self.director.exitLevel()
                elif event.key == K_RETURN:
                    # Exit to main menu
                    mixer.music.unload()
                    self.director.exitLevel()
                    
    def draw(self,screen):
        screen.fill(BLACK)
        screen.blit(self.background,[0,0])