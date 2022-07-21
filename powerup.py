import pygame
from configs import *
from manager import Manager
from sprite import *

# Class that modifies different aspects of the player or its weapon
class Effect:
    def __init__(self, target, apply, amount):
        # Modify player or wepoan
        self.target = target
        # Kind of power up
        self.apply = apply
        # Every powerup, will last the same
        self.timer = 500
        # Quantity to modify
        self.amount = amount
    
    def apply_effect(self, player):
        # Modify player
        if self.target == "player":
            # If the powerup is healthup
            if self.apply == "healthup":
                # We add one heart to our player's health
                # There's no limit in our player health
                player.health += self.amount
            # If the powerup is healthup
            elif self.apply == "healthdown":
                # We check its life
                if(player.health > 0):
                    # We take away one heart to our player's health
                    player.health -= self.amount
        # Modify weapon
        elif self.target == "weapon":
            # If we take a weapon powerup, we're no longer using our default weapon
            player.level.weapon.default = False
            # If the powerup is damage
            if self.apply == "damage":
                # We multiply our weapon's damage 
                player.level.weapon.damage *= self.amount
            # If the powerup is range
            elif self.apply == "range":
                # We add range to our weapon 
                player.level.weapon.bullet_lifetime += self.amount
            # If the powerup is shotgun
            elif self.apply == "shotgun":
                # We change our weapong to a shotgun
                player.level.weapon.change_weapon(SHOTGUN)
            # If the powerup is bomb
            elif self.apply == "bomb":
                # We active our special attack using our dead's friend body (Martina la Sardina)
                player.level.weapon.activate_martina()
            # We set a life limit for the weapon, so the powerup won't last forever
            player.level.weapon.weapon_lifetime = self.timer

# Class that defines a power up                     
class PowerUp(Sprit):
    def __init__(self,rect, image, level):
        self.rect = rect
        self.image = Manager.loadImageScaled(image, 100, 100).convert_alpha()
        # By default, the power up is not used
        self.used = False
        # We apply the powerup to the player in the current level
        self.player = level.player
        self.level = level
    
    # Check if it has effect
    def check_effect(self, effect):
        return effect is not None

    def update(self, time, effect):
        # If the powerup has an effect and was used
        if self.used and self.check_effect(effect):
            # We apply the effect
            self.effect.apply_effect(self.player)
            # And kill the powerup's sprite
            self.kill()
    
    def draw(self, screen):
        aux = self.level.camera.apply(self)
        screen.blit(self.image, aux)
         

class HealthUp(PowerUp):
    def __init__(self,rect, player):
        pygame.sprite.Sprite.__init__(self)
        image = HEART
        super().__init__(rect, image, player)
        self.effect = Effect("player", "healthup", 1)

    def update(self, time):
        super().update(time, self.effect)
    
    def draw(self, screen):
        super().draw(screen)

class MoreDamage(PowerUp):
    def __init__(self,rect, player):
        pygame.sprite.Sprite.__init__(self)
        image = BULLET
        super().__init__(rect, image, player)
        self.effect = Effect("weapon", "damage", 10)

    def update(self, time):
        super().update(time, self.effect)

    def draw(self, screen):
        super().draw(screen)

class MoreRange(PowerUp):
    def __init__(self,rect, player):
        pygame.sprite.Sprite.__init__(self)
        image = BULLET
        super().__init__(rect, image, player)
        self.effect = Effect("weapon", "range", 2)

    def update(self, time):
        super().update(time, self.effect)

    def draw(self, screen):
        super().draw(screen)

class MartinaBomb(PowerUp):
    def __init__(self,rect, player):
        pygame.sprite.Sprite.__init__(self)
        image = MARTINA
        super().__init__(rect, image, player)
        self.effect = Effect("weapon", "bomb", 1)

    def update(self, time):
        super().update(time, self.effect)

    def draw(self, screen):
        super().draw(screen)
    
class ShotGun(PowerUp):
    def __init__(self,rect, player):
        pygame.sprite.Sprite.__init__(self)
        image = SHOTGUN_PNG
        super().__init__(rect, image, player)
        self.effect = Effect("weapon", "shotgun", 0)

    def update(self, time):
        super().update(time, self.effect)

    def draw(self, screen):
        super().draw(screen)