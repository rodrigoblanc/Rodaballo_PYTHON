import pygame 
from pygame.locals import *
from configs import *
import random
from powerup import ShotGun
from sprites import *
from manager import *
from sprite import *
from character import *
from genericEnemy import *

# Class where we declare a basic enemy. Every level can have several of them
class enemyBasic(genericEnemy):
    def __init__(self,life, position, level,weapon):
        super().__init__(position,level)
        self.life = life
        self.direction = 'stand_left'
        self.speed = self.speed * 0.4 *random.uniform(0.4,0.9)
        self.jump()
        self.weapon = weapon
        
    # Implmentation of a basic AI for the enemy's movement
    def move_cpu(self):
        # Declare the range of approach to the player, so that the enemy's sprite does not remain on top of the player's
        desired_distance = 200
        # Declare the desired distance for the enemy to start chasing the player
        start_movement = 500
        # Player's rect
        rect_player = self.level.player.rect.x
        # Enemy's rect
        rect_enemy = self.rect.x
        
        # Check the distante between our player and the enemy
        distance = rect_enemy - rect_player
        # Check they're in the desired distance so the enemy can start moving
        if abs(distance) < start_movement:
            # If the player is to the left of the enemy, the enemy moves to the left
            if rect_player < rect_enemy:
                self.direction = 'left'
                # If the enemy is within range, stop moving but keep aiming left
                if rect_enemy < rect_player + desired_distance:
                    self.direction = 'stand_left'
            # If the player is to the right of the enemy, the enemy moves to the right
            elif rect_player > rect_enemy:
                self.direction = 'right'
                # If the enemy is within range, stop moving but keep aiming right
                if rect_enemy > rect_player - desired_distance:
                    self.direction = 'stand_right'
     
    def update(self, time):
        # We update its position and where it aims
        self.move_cpu()
        # Update its weapon and how/when it shoots
        self.weapon.update(self,time,0,0)
        self.weapon.shoot()
        self.check_horizontal_collisions()
        # Check if there are bullets from the player that hit the enemy
        hits = pygame.sprite.spritecollide(self,self.level.bullet_group,False)
        for hit in hits:
            # Player's bullets have 'good' in the atributte tea
            # Other enemy's have 'bad', so if other enemy hit this enemy, it doesn't affet it's life
            if hit.team == 'good':
                self.life = self.life - hit.damage
                hit.kill()
        # Check this enemy's life
        if self.life <= 0:
            # Kill the weapon's sprite
            self.weapon.kill()
            # Kill this enemy's sprite
            self.kill()
        # We modify our horizontal movement, depending on the direction
        # This direction will change depending on the player's position
        if self.direction == 'right':
            self.move_x(1, time)
        elif self.direction == 'left':
            self.move_x(-1, time)
        else:
            self.mov_direction.x = 0
        if self.direction == 'jump':
            if self.isjumping == True and self.in_air == False:
                self.jump()

        self.check_vertical_collisions()

# Class where we declare a enemy with a shotgun. Every level can have several of them
class enemyShotgun(genericEnemy):
    def __init__(self,life, position, level,weapon):
        super().__init__(position,level)
        self.life = life
        self.direction = 'stand_left'
        self.speed = self.speed * 0
        self.jump()
        self.weapon = weapon

    def move_cpu(self):
        if self.level.player.rect.left < self.rect.left:
            self.direction = 'stand_left'
        else: 
            self.direction = 'stand_right'

    def update(self, time):
        # We update its position and where it aims
        self.move_cpu()
        # Update its weapon and how/when it shoots
        self.weapon.update(self,time,0,0)
        self.weapon.shoot()
        self.check_horizontal_collisions()
        # Check if there are bullets from the player that hit the enemy
        hits = pygame.sprite.spritecollide(self,self.level.bullet_group,False)
        for hit in hits:
            # Player's bullets have 'good' in the atributte tea
            # Other enemy's have 'bad', so if other enemy hit this enemy, it doesn't affet it's life
            if hit.team == 'good':
                self.life = self.life - hit.damage
                hit.kill()
        # Check this enemy's life
        if self.life <= 0:
            # If it dies, it will drop a shotgun as a powerup
            aux = (ShotGun(pygame.Rect(self.rect.x, self.rect.y, 40,40), self.level))
            self.level.powerups.add(aux) 
            self.level.entities.add(aux)
            # Kill the weapon's sprite
            self.weapon.kill()
            # Kill this enemy's sprite
            self.kill()
        # We modify our horizontal movement, depending on the direction
        # This direction will change depending on the player's position
        if self.direction == 'right':
            self.move_x(1, time)
        elif self.direction == 'left':
            self.move_x(-1, time)
        else:
            self.mov_direction.x = 0
        if self.direction == 'jump':
            if self.isjumping == True and self.in_air == False:
                self.jump()
        self.check_vertical_collisions()

# Class where we declare the boss 
class enemyBoss(genericEnemy):
    def __init__(self,life, position, level,weapon1,weapon2,weapon3, image, x, y):
        super().__init__(position,level)
        self.image = Manager.loadImageScaled(image, x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.life = life
        self.direction = 'stand_left'
        self.speed = 0
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.weapon3 = weapon3     

    def move_cpu(self):
        # The boss won't move
        pass 

    def update(self, time):
        self.move_cpu()
        # Has three weapons
        self.weapon1.update(self,time,0,10)
        self.weapon2.update(self,time,40,100)
        self.weapon3.update(self,time,0,200)

        # Update its weapons and how/when they shoot
        if (self.level.player.rect.y > (self.weapon1.rect.y -30)) and (self.level.player.rect.y < (self.weapon1.rect.y +30)):
            self.weapon1.shoot()
        if (self.level.player.rect.y > (self.weapon2.rect.y -50)) and (self.level.player.rect.y < (self.weapon2.rect.y +50)):
            self.weapon2.shoot()
        if (self.level.player.rect.y > (self.weapon3.rect.y -30)) and (self.level.player.rect.y < (self.weapon3.rect.y +30)):
            self.weapon3.shoot()

        # Check if there are bullets from the player that hit the enemy
        hits = pygame.sprite.spritecollide(self,self.level.bullet_group,False)
        for hit in hits:
            # Player's bullets have 'good' in the atributte tea
            # Other enemy's have 'bad', so if other enemy hit this enemy, it doesn't affet it's life
            if hit.team == 'good':
                self.life = self.life - hit.damage
                hit.kill()

        # Every time it loses a certain amount of life, it will lose a weapon
        if self.life <= 100:
            self.weapon3.kill()
            
        if self.life <= 50:
            self.weapon1.kill()
            
        if self.life <= 0:
            self.weapon2.kill()
            self.kill()
            
        self.check_vertical_collisions()

