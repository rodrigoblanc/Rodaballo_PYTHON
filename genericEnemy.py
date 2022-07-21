from pygame.locals import *
from configs import *
from sprites import *
from manager import *
from sprite import *
from character import *

# Declares a character that will try to kill our main character
class genericEnemy(Character):
    def __init__(self, position, level):
        super().__init__(position,level)
        self.image = Manager.loadImageScaled(ENEMY, 100,100)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    # Enemies default position = no movement + standing left
    def move_cpu(self):
        self.direction = 'stand_left'
    
    # Check horizontal collisions
    def check_horizontal_collisions(self):
        # First apply the horizontal movement
        self.rect.x += self.mov_direction.x
        # Then check against level sprite group / platforms
        for sprite in self.level.spriteGroup.sprites():
            if sprite.rect.colliderect(self.rect):
                self.direction = 'jump'
                self.isjumping = True
                # If it's moving left, it's (probably) colliding with something on the left
                if self.mov_direction.x < 0:
                    # We limit the enemy's rect 
                    self.rect.left = sprite.rect.right
                # If not, we do the opposite to the right side
                elif self.mov_direction.x > 0:
                    # We limit the enemy's rect 
                    self.rect.right = sprite.rect.left
                # And stop moving
                self.mov_direction.x = 0