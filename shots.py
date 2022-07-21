import pygame 
import random
from pygame.locals import *
from configs import *
from sprite import Sprit
from sprites import *
from manager import *
import math

class Bullet(Sprit):

     def __init__(self,position,direction,angle,lifetime,damage, level,team):
         pygame.sprite.Sprite.__init__(self)
         self.team = team
         self.angle = angle
         self.lifetime = lifetime
         self.damage = damage
         self.level = level
         self.position = position
         if direction == "stand_right" :
             self.direction = "right"
         elif direction == "right":
            self.direction = "right"
         else:
             self.direction = "left"
         if direction == "left" :
            self.image = pygame.transform.rotate(Manager.loadImage("disparo.png"),90 -angle)
            self.position[0]-50
         else :
            self.image = pygame.transform.rotate(Manager.loadImage("disparo.png"),-90 + angle)
            self.position[0]+50
         self.position[1]-30
         self.rect = self.image.get_rect()
         self.rect.topleft = self.position
         self.frame = 0

     def update(self,time):

         self.lifetime -= time
         if self.direction == 'left':
             self.rect.x -= MOVEMENT *2 * (math.cos(self.angle).real) * time
             self.rect.y += MOVEMENT *2 * (math.sin(self.angle).real) * time

         if self.direction == 'right':
             self.rect.x += MOVEMENT *2 * (math.cos(self.angle).real) * time
             self.rect.y += MOVEMENT *2 * (math.sin(self.angle).real) * time     
         if self.lifetime < 0:
             self.kill()   
         self.check_horizontal_collisions()

     def draw(self, screen):
        aux = self.level.camera.apply(self)
        screen.blit(self.image, aux)

     def check_horizontal_collisions(self):
        # Checks against the level's spriteGroup, so we bullet dies when it
        # hits and obstacle
        if(pygame.sprite.spritecollide(self,self.level.spriteGroup,False)):
            self.kill()
        # Checks against the player, takes 1 of heath away and dies
        if(self.rect.colliderect(self.level.player.rect)):
            if(self.team == "bad"):
                self.level.player.health -= 1
                self.kill()
        
         
class Weapon(Sprit):

     def __init__(self,position, direction,number_of_bullets,dispersion,reload, bullet_lifetime, weaponID,damage, weapon_lifetime,level,team):
         pygame.sprite.Sprite.__init__(self)
         if direction == "stand_left" :
             self.direction = "left"
         elif direction == "left":
            self.direction = "left"
         else:
             self.direction = "right"
         self.is_fliped = False
         self.team = team
         self.bullet_lifetime = bullet_lifetime 
         self.damage = damage
         self.position = position
         self.direction = direction
         self.number_of_bullets = number_of_bullets
         self.dispersion = dispersion
         self.reload_time = reload
         self.last_shot = reload
         self.weapon_lifetime = weapon_lifetime
         self.level = level
         self.adjust_x = 0
         self.adjust_y = 0
         self.sfx = Manager.loadSound(PLACEHOLDERSFX)
         if weaponID == 0:
             self.sfx = Manager.loadSound(HANDGUNSFX)
             self.image = Manager.loadImageScaled("pistol(1).png", 25, 25)
             self.adjust_x = 35
             self.adjust_y = 25
         if weaponID == 1:
             self.sfx = Manager.loadSound(HANDGUNSFX)
             self.image = Manager.loadImageScaled("pistol.png", 3, 3)
             self.adjust_x = 0
             self.adjust_y = 40
         if weaponID == 2:
            self.sfx = Manager.loadSound(SHOOTGUNSFX)
            self.image = Manager.loadImageScaled("shotgun.png", 90, 90)
            self.adjust_x = 0
            self.adjust_y = 0
         if weaponID == 3:
            self.sfx = Manager.loadSound(ACIDSFX)
            self.image = Manager.loadImageScaled("acido.png", 20, 20)
         if weaponID == 4:
            self.sfx = Manager.loadSound(SHOOTGUNSFX)
            self.image = Manager.loadImageScaled("shotgun(1).png", 40, 40)
            self.adjust_x = 20
            self.adjust_y = 25


         self.image = pygame.transform.rotate(self.image,90)
         self.image = pygame.transform.flip(self.image,True,False)
         self.rect = self.image.get_rect()
         self.rect.center = position
         self.frame = 0

    # Function to get our default weapon -> handgun
     def get_default_weapon(self):
         self.__init__(self.position, self.direction, *HANDGUN, self.level, self.team)

    # Function to change our default weapon to any other "good" weapon
     def change_weapon(self, weapon):
         self.__init__(self.position, self.direction, *weapon, self.level, self.team)


     def setTeam(self,team):
         self.team = team

     def activate_martina(self):
         # Define the range of the explosion
         start_explosion = 500
         rect_player = self.level.player.rect.x
         # We check all the enemies in the enemy group
         for sprite in self.level.enemy_group:
             # If they're in the range of the explosion, we kill their sprite
             if abs(sprite.rect.x - rect_player) < start_explosion:
                 self.kill_enemy(sprite)
         
     def kill_enemy(self, sprite):
         # We first kil the enemy's weapon sprite 
         sprite.weapon.kill()
         # And then the enemy's sprite
         sprite.kill()

     def update(self, player,time,offset_x,offset_y):               
        self.rect.y = player.rect.y + (self.adjust_y + offset_y)
        
        if ((player.direction == 'right') or (player.direction == 'stand_right')):
            if self.is_fliped == False:
                self.image = pygame.transform.flip(self.image,True,False)
                player.image = pygame.transform.flip(player.image,True,False)

                self.is_fliped = True
            self.rect.x = player.rect.x + (self.adjust_x + offset_x)
        if ((player.direction == 'left') or (player.direction == 'stand_left')):
            if self.is_fliped == True:
                self.image = pygame.transform.flip(self.image,True,False)
                player.image = pygame.transform.flip(player.image,True,False)
                self.is_fliped = False
            self.rect.x = player.rect.x - offset_x

        self.direction = player.direction
        self.last_shot += time
        self.weapon_lifetime -= 1
        if self.weapon_lifetime < 0:
            self.get_default_weapon()
            self.default = True

     def shoot(self):
         if(self.last_shot >= self.reload_time):
            if(self.team == "good"):
                self.sfx.play()
            for i in range(self.number_of_bullets):
                aux = 1
                aux = (Bullet((self.rect.center),self.direction,(random.uniform(-0.6,0.6))*self.dispersion,self.bullet_lifetime,self.damage, self.level,self.team))
                self.level.bullet_group.add(aux)
                self.level.entities.add(aux)
            self.last_shot = 0

     def draw(self, screen):
        aux = self.level.camera.apply(self)
        screen.blit(self.image, aux)
         





