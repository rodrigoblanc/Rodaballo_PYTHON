from level import Level
from player import *
from configs import *
from pygame import mixer
from powerup import *
from levelMenu import *
from plataform import *
from shots import *
from level import *
from customCamera import *
from manager import Manager
import itertools
from enemies import *
from menu import *
from deadLevel import *
from level2 import *
from levelpass import *

class Level1(Level):
    def __init__(self,director, auxVolume) :
        super().__init__(director)
        mixer.music.unload()
        # Each level will have its own song and volume
        self.auxVolume = auxVolume
        mixer.music.load('Music/action.mp3')
        mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.auxVolume)
        # We manage the sounds with our resource manager
        Manager.loadSound(SHOOTGUNSFX).set_volume(self.auxVolume)
        Manager.loadSound(HANDGUNSFX).set_volume(self.auxVolume)
        self.player = MainCharacter((CHARACTER_SPAWN_WIDTH+70,CHARACTER_SPAWN_HEIGHT), self)
        total_level_width  = 600*32 # calculate size of level in pixels
        total_level_height = 400*32
        # Custom camera for scroll
        self.camera = CustomCamera(total_level_width, total_level_height)
        self.time = CLOCK.tick_busy_loop(FPS)
        self.menu = LevelMenu(director)
        self.screen = director.screen
        self.game_over = False
        self.background = Manager.loadImage("fondo720.png")

        # All groups declaration
        self.spriteGroup = pygame.sprite.Group()
        # Group where we store all sprites
        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        # Group where we store bullets
        self.bullet_group = pygame.sprite.Group()
        self.entities.add(self.bullet_group)
        # Group where we store enemies
        self.enemy_group = pygame.sprite.Group()
        # Group where we store base platform: sidewalk
        self.platform = pygame.sprite.Group()
        # Group with power ups
        self.powerups = pygame.sprite.Group()

        # We add all the different types of sprites to the scene
        self.add_enemies()
        self.add_plaftforms()
        self.add_powerups()
        self.add_boss()
        self.add_weapons()

    def add_enemies(self):
        # Adds all enemies and its weapons to entities and enemies groups

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)

        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+1000,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)
        
        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+2300,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(30,(CHARACTER_SPAWN_WIDTH+2350,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2400,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2400,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2400,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2400,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2450,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(30,(CHARACTER_SPAWN_WIDTH+2500,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+3900,CHARACTER_SPAWN_HEIGHT+410 ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)
        
        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+3900,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        # Enemigo 2
        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(50,(CHARACTER_SPAWN_WIDTH+1550,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(50,(CHARACTER_SPAWN_WIDTH+4500,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)


    def add_plaftforms(self):
        # We add all platforms to all the groups needed 
        platform_list = []

        sidewalk_platform = Plataform(pygame.Rect(SPAWN, 700, 50000, 50), "empty", self)
        self.platform.add(sidewalk_platform)
        self.entities.add(sidewalk_platform)
        platform_list.append(sidewalk_platform)

        plat6 = Plataform(pygame.Rect(SPAWN, 350, 75, 500), WALLPATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        car = Plataform(pygame.Rect(200+SPAWN, 625, 150,75), CARPATH, self)
        self.spriteGroup.add(car)
        self.entities.add(car)
        platform_list.append(car)

        plat1 = Plataform(pygame.Rect(400+SPAWN, 550, 200,25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat1)
        self.entities.add(plat1)
        platform_list.append(plat1)

        plat1_1 = Plataform(pygame.Rect(400+SPAWN, 300, 200,25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat1_1)
        self.entities.add(plat1_1)
        platform_list.append(plat1_1)

        plat2 = Plataform(pygame.Rect(600+SPAWN, 425, 200,25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat2)
        self.entities.add(plat2)
        platform_list.append(plat2)

        plat2_1 = Plataform(pygame.Rect(800+SPAWN, 250, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat2_1)
        self.entities.add(plat2_1)
        platform_list.append(plat2_1)

        car2 = Plataform(pygame.Rect(800+SPAWN, 650, 150,75), CARPATH, self)
        self.spriteGroup.add(car2)
        self.entities.add(car2)
        platform_list.append(car2)

        plat3 = Plataform(pygame.Rect(1000+SPAWN, 500, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat3)
        self.entities.add(plat3)
        platform_list.append(plat3)

        plat4 = Plataform(pygame.Rect(1200+SPAWN, 450, 200,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat4)
        self.entities.add(plat4)
        platform_list.append(plat4)

        car3 = Plataform(pygame.Rect(1300+SPAWN, 650, 175,75), CARPATH, self)
        self.spriteGroup.add(car3)
        self.entities.add(car3)
        platform_list.append(car3)

        plat5 = Plataform(pygame.Rect(1400+SPAWN, 600, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat5)
        self.entities.add(plat5)
        platform_list.append(plat5)

        plat5_1 = Plataform(pygame.Rect(1450+SPAWN, 250, 200,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat5_1)
        self.entities.add(plat5_1)
        platform_list.append(plat5_1)

        plat6 = Plataform(pygame.Rect(1600+SPAWN, 450, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(1900+SPAWN, 400, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        car4 = Plataform(pygame.Rect(2000+SPAWN, 650, 175,75), CARPATH, self)
        self.spriteGroup.add(car4)
        self.entities.add(car4)
        platform_list.append(car4)

        plat6 = Plataform(pygame.Rect(2200+SPAWN, 350, 75, 400), WALLPATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(2400+SPAWN, 550, 200,25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(2600+SPAWN, 400, 200,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(2700+SPAWN, 200, 100,25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(2900+SPAWN, 350, 100,50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(3300+SPAWN, 300, 75, 450), WALLPATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(3350+SPAWN, 400, 200, 25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(3700+SPAWN, 550, 75, 175), WALLPATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(3900+SPAWN, 575, 300, 25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(4200+SPAWN, 550, 200, 50), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(4300+SPAWN, 550, 200, 25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(5000+SPAWN, 550, 200, 25), PLATFORM1PATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        plat6 = Plataform(pygame.Rect(5200+SPAWN, 475, 50, 300), WALLPATH, self)
        self.spriteGroup.add(plat6)
        self.entities.add(plat6)
        platform_list.append(plat6)

        # Invisible platform to the left's spawn
        left_limit_platf = Plataform(pygame.Rect(-10+SPAWN, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(left_limit_platf)
        self.entities.add(left_limit_platf)
        platform_list.append(left_limit_platf)

        # Invisible platform to the bosse's right
        right_limit_platf = Plataform(pygame.Rect(6100+CHARACTER_SPAWN_WIDTH, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(right_limit_platf)
        self.entities.add(right_limit_platf)
        platform_list.append(right_limit_platf)

        # Group with all collision platforms
        self.all_platforms = pygame.sprite.Group()
        for x in itertools.product(platform_list):
            self.all_platforms.add(x)

    def add_powerups(self):
        # We add all power ups to all the groups needed 

        health_up = HealthUp(pygame.Rect(800+SPAWN, 150, 150,150), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)
        health_up = HealthUp(pygame.Rect(1500+SPAWN, 150, 150,150), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)
        health_up = HealthUp(pygame.Rect(3000+SPAWN, 600, 150,150), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)
        health_up = HealthUp(pygame.Rect(5100+SPAWN, 600, 150,150), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)
        health_up = HealthUp(pygame.Rect(5000+SPAWN, 600, 150,150), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)

        more_damage = MoreDamage(pygame.Rect(3500+SPAWN, 600, 200,200), self)
        martina = MartinaBomb(pygame.Rect(2100+SPAWN, 525, 100,100), self)

        self.powerups.add(health_up)
        self.powerups.add(more_damage)
        self.powerups.add(martina)

        self.entities.add(health_up)
        self.entities.add(more_damage)
        self.entities.add(martina)

    def add_boss(self):
        # We add the final boss and its weapons
        boss_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        boss_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        boss_weapon3 = Weapon((self.player.rect.center),"left",*MACHINEGUNE, self,'bad')
        self.entities.add(boss_weapon1)
        self.entities.add(boss_weapon2)
        self.entities.add(boss_weapon3)
        self.boss_kim = (enemyBoss(120,(CHARACTER_SPAWN_WIDTH+5600,CHARACTER_SPAWN_HEIGHT ), self,boss_weapon1,boss_weapon2,boss_weapon3, KIM, 300, 300))
        self.enemy_group.add(self.boss_kim)
        self.entities.add(self.boss_kim)

    def add_weapons(self):
        self.weapon = Weapon((self.player.rect.center),"left",*HANDGUN, self,'good')
        self.entities.add(self.weapon)

    def update(self,direction):
        pygame.display.update()
        mixer.music.unpause()
        if not(mixer.music.get_busy()):
            # We change the music to a specific sound for Level1
            mixer.music.load('Music/action.mp3')
            # Each sound can sound louder or lower, so we change its volume in every level
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)
        # Update the clock, we call this method once per frame and our game will never run at more than 50 fps
        self.time = CLOCK.tick_busy_loop(FPS)
        # We update all the elements declared in this level
        self.player.update(self.player.desired_direction, self.time)
        self.weapon.update(self.player,self.time,0,0)
        self.enemy_group.update(self.time)
        self.bullet_group.update(self.time)
        self.camera.update(self.player)
        self.powerups.update(self.time)
        self.boss_kim.update(self.time)
        # Check our player's health
        if self.player.health < 1:
            self.game_over = True
            # If our player's dead, we can try the level again
            menuP = FailLevel(self.director, Level1(self.director, self.auxVolume))
            self.director.changeLevel(menuP) 
        # The level is passed if we kill the boss
        if self.boss_kim.life <= 0:
            self.director.changeLevel(LevelPass(self.director, Level2(self.director, self.auxVolume), self.auxVolume))

    def events(self,events):
        # Different options for different keys pressed
        for event in events:
            if event.type == KEYDOWN :
                # We notify the director if we want to exit
                if event.key == K_ESCAPE:
                    self.director.exitLevel()
                if event.key == K_SPACE:
                    self.player.isjumping = True
                    self.player.update('jump', self.time)
                if event.key == K_p:
                    self.weapon.shoot()   
                if event.key == K_q:
                    # Change to pause menu
                    self.director.stackLevel(self.menu) 
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a: 
                    self.player.desired_direction ='stand_left'
                if event.key == pygame.K_d:
                    self.player.desired_direction ='stand_right'
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_a]:
            self.player.desired_direction ='left'
        if pressed_key[K_d]:
            self.player.desired_direction ='right'


    def draw(self,screen):
        # We draw all our sprites, stored in the group self.entities
        screen.fill(BLACK)
        screen.blit(self.background,[0,0])
        # We apply each element to the camera, so we can scroll
        for e in self.entities:
            screen.blit(e.image, self.camera.apply(e)) 
        super().draw(screen)
        pygame.display.flip()