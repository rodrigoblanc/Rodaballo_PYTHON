from player import *
from configs import *
from pygame import mixer

class Director():
    def __init__(self):
        # Init pygame's library
        pygame.init()
        # Create our game screen
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.DOUBLEBUF)
        pygame.display.set_caption("Rodaballo do Carallo")
        # Get pygame's clock
        self.clock = pygame.time.Clock()
        # Create our main character
        self.player = MainCharacter((CHARACTER_SPAWN_HEIGHT,CHARACTER_SPAWN_WIDTH), self)
        # Set the exit game flag to false
        self.level_end = False
        # Scene's stack
        self.stack = []

    def gameLoop(self,level):
        # Set the exit game flag to false
        self.level_end = False
        # Clear all the events given before entering the loop
        pygame.event.clear()
        # Pause the music
        mixer.music.pause()
        while not self.level_end : 
            # Sincronize the game to 50 fps
            self.time = self.clock.tick(FPS)
            # Pass the events to the scene
            level.events(pygame.event.get())
            # Update the scene
            level.update(self.time)
            # Draw the screen
            level.draw(self.screen)
            pygame.display.flip()

    def execute(self):
        # While there's scenes on the stack, we'll execute the one on top
        while(len(self.stack)>0):
            # The scene to execute is the one on top of the stack
            level = self.stack[len(self.stack)-1]
            # Execute the loop
            self.gameLoop(level)

    def exitLevel(self):
        self.level_end = True
        # We pop the current scene from the stack
        if(len(self.stack)>0):
            self.stack.pop()
    
    def exitGame(self):
        # Empty the scene's stack
        self.stack = []
        self.level_end = True

    def changeLevel(self,level):
        # We pop the current scene from the stack
        self.exitLevel()
        # We put the previous scene on top of the stack
        self.stack.append(level)

    def stackLevel(self,level):
        self.level_end = True
        # We put the previous scene on top of the stack 
        self.stack.append(level)