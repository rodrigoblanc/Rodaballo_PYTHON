import pygame 
from pygame.locals import *
from configs import *
import sys
from sprites import *
from manager import *
from sprite import *

# Class that declares characters with movement
class Character(Sprit): 
    def __init__(self, position, level):
        super().__init__()
        self.info = pygame.display.Info()
        self.frame = 0
        # Default position: no movement + looking right
        self.direction = "stand_right"
        # We declare which sprites to use for each type of position / movement 
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        # Variables to manage jumping
        # Detect SPACE button was pressed
        self.isjumping = False
        # Character on air while jumping
        self.in_air = True
        # We store x,y values for the movement
        self.mov_direction = pygame.math.Vector2(0,0)
        self.speed = MOVEMENT
        self.gravity = GRAVITY
        # jump_speed is a negative variable, so the character moves up when its jumping
        self.jump_speed = JUMP_HEIGHT
        self.level = level
    
    def draw(self, screen):
        aux = self.level.camera.apply(self)
        screen.blit(self.image, aux)

    def quit(): 
        sys.exit()

    # Returns the corresponding frame  
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    # Change the sprite depending on the frame
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    # Change the sprite depending on the key pressed
    def change_sprite(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
        elif direction == 'right':
            self.clip(self.right_states)
        elif direction == 'stand_left':
            self.clip(self.left_states[0])
        elif direction == 'stand_right':
            self.clip(self.right_states[0])
        # Define image with the current sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    # Applies gravity force
    def apply_gravity(self):
        # We add the gravity value to our character's y component
        self.mov_direction.y += self.gravity
        self.rect.y += self.mov_direction.y

    # Character jump
    def jump(self):
        # We set a negative value to our character's y component
        self.mov_direction.y = self.jump_speed
        # We reset the SPACE button pressed 
        self.isjumping = False
        # Now it's in the air
        self.in_air = True

    # Check horizontal collisions
    def check_horizontal_collisions(self):
        # First apply the horizontal movement
        self.rect.x += self.mov_direction.x
        # Then check against level sprite group / platforms
        for sprite in self.level.spriteGroup.sprites():
            # If the character's rect collide with any rect in spriteGroup, we modify its position
            if sprite.rect.colliderect(self.rect):
                # If we're moving left, we're (probably) colliding with something on the left
                if self.mov_direction.x < 0:
                    # We limit our character's rect 
                    self.rect.left = sprite.rect.right
                # If not, we do the opposite to the right side
                elif self.mov_direction.x > 0:
                    # We limit our character's rect 
                    self.rect.right = sprite.rect.left
                # And stop moving
                self.mov_direction.x = 0

    # Check vertical collisions
    def check_vertical_collisions(self):
        # First apply the vertical movement
        self.apply_gravity()
        # Then check against level sprite group / platforms + sidewalk
        for sprite in self.level.all_platforms.sprites():
            # If the character's rect collide with any platform/ground, we modify its position
            if sprite.rect.colliderect(self.rect):
                # If we're jumping, we're (probably) colliding with something underneath us
                if self.mov_direction.y > 0:
                    # We limit our character's rect 
                    self.rect.bottom = sprite.rect.top
                # If not, we're colliding with something above us
                elif self.mov_direction.y < 0:
                    # We limit our character's rect 
                    self.rect.top = sprite.rect.bottom
                # We cancel the gravity force
                self.mov_direction.y = 0
                # And stop jumping
                self.in_air = False                

    # Horizontal scroll: depends on the direction and speed of the character
    def move_x(self, direction, time):
        if direction == 1:
            # Right movement
            self.mov_direction.x = self.speed * time
        else:
            # Left movement
            self.mov_direction.x = -self.speed * time

    def update(self, direction, time):
        # We modify our horizontal movement, depending on the direction, which changes when we pressed keys
        if direction == 'right':
            self.direction = 'right'
            self.move_x(1, time)
        elif direction == 'left':
            self.move_x(-1, time)
            self.direction= 'left'
        else:
            self.mov_direction.x = 0
         # We modify our vertical movement
        if direction == 'jump':
            # If SPACE bar was pressed and the character's not on air, it can jump
            if self.isjumping == True and self.in_air == False:
                self.jump()

        self.change_sprite(direction)
        self.check_vertical_collisions()
        self.check_horizontal_collisions()
    