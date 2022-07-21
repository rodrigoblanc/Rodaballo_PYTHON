from menu import *
from player import *
from configs import *
from director import *

pygame.mixer.pre_init(88200,16,4, 8192)
pygame.mixer.init()
# Run by user
if __name__ == "__main__":
    pygame.init()
    director = Director()
    # Scene with the initial screen
    startScene = Menu(director)
    # We tell the director to stack the scene
    director.stackLevel(startScene)
    # And to start
    director.execute()
    pygame.quit ()