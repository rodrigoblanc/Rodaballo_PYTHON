from player import *
from configs import *
from levelMenu import *
from plataform import *
from shots import *
from level import *

# Class that implements the lateral screoll: it adds an offset to our entities when drawing them
class CustomCamera(object):
    def __init__(self, width, height):
        self.state = Rect(CHARACTER_SPAWN_HEIGHT, CHARACTER_SPAWN_WIDTH, width, height)
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
        
    def update(self, target):
        self.state = self.complex_camera(self.state, target.rect)
    
    def complex_camera(self, camera, target_rect):
        # we want to center target_rect
        x = -target_rect.center[0] + WIDTH/2 
        y = -target_rect.center[1] + HEIGHT/2
        # move the camera. Let's use some vectors so we can easily substract/multiply
        camera.topleft += (pygame.Vector2((x, y)) - pygame.Vector2(camera.topleft)) * 0.06 # add some smoothness coolnes
        # set max/min x/y so we don't see stuff outside the world
        camera.x = max(-(camera.width-WIDTH), max(0, camera.x))
        camera.y = max(-(camera.height-HEIGHT), max(0, camera.y))
        
        return camera