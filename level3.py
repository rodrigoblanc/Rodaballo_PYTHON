from director import Director
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
from levelpass import *

class Level3(Level):
    def __init__(self,director, auxVolume) :
        super().__init__(director)
        # Each level will have its own song and volume
        self.auxVolume = auxVolume
        mixer.music.unload()
        mixer.music.load('Music/king_of_the_hill.mp3')
        pygame.mixer.music.set_volume(self.auxVolume)
        mixer.music.play(-1)
        # We manage the sounds with our resource manager
        Manager.loadSound(SHOOTGUNSFX).set_volume(self.auxVolume)
        Manager.loadSound(HANDGUNSFX).set_volume(self.auxVolume)
        self.player = MainCharacter((CHARACTER_SPAWN_WIDTH+100,CHARACTER_SPAWN_HEIGHT-200), self)
        total_level_width  = 600*32 # calculate size of level in pixels
        total_level_height = 400*32
        # Custom camera for scroll
        self.camera = CustomCamera(total_level_width, total_level_height)        
        self.time = CLOCK.tick_busy_loop(FPS)
        self.menu = LevelMenu(director)
        self.game_over = False
        # levelInit allows us to know when the level3 starts
        # = true -> screen showing the context of the story previous to the level
        # = false -> level3 starts
        self.levelInit = True
        self.background = Manager.loadImage("ViajeEEUUCentral.png")

        # All groups declaration
        self.spriteGroup = pygame.sprite.Group()
        # Group where we store all sprites
        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        # Group where we store bullets
        self.bullet_group = pygame.sprite.Group()
        self.entities.add(self.bullet_group)
        #Player weapon
        self.weapon = Weapon((self.player.rect.center),"left",*HANDGUN, self,'good')
        self.entities.add(self.weapon)

        # Group where we store enemies
        self.enemy_group = pygame.sprite.Group()
        # Group where we store base platform: sidewalk
        self.platform = pygame.sprite.Group()
        # Group with power ups
        self.powerups = pygame.sprite.Group()

        # We add all the different types of sprites to the scene
        self.add_enemies()
        self.add_platforms()
        self.add_powerups()
        self.add_boss()
        
    def add_enemies(self):
        self.enemy_group = pygame.sprite.Group()

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+500,600), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+600,600), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+700,600), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+2900,400), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+4500,550), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+4500,550), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+4500,550), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+4600,550), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(20,(CHARACTER_SPAWN_WIDTH+4600,550), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(50,(CHARACTER_SPAWN_WIDTH+500,0), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(30,(CHARACTER_SPAWN_WIDTH+650,300), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(50,(CHARACTER_SPAWN_WIDTH+1600,100), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(40,(CHARACTER_SPAWN_WIDTH+1850,0), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(40,(CHARACTER_SPAWN_WIDTH+3600,100), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(40,(CHARACTER_SPAWN_WIDTH+4500,550), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(40,(CHARACTER_SPAWN_WIDTH+5000,550), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux2 = (enemyShotgun(40,(CHARACTER_SPAWN_WIDTH+5400,0), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

    def add_platforms(self):
        platform_list = []
        sidewalk_platform = Plataform(pygame.Rect(SPAWN, 700, 50000, 50), "empty", self)
        self.platform.add(sidewalk_platform)
        self.entities.add(sidewalk_platform)
        platform_list.append(sidewalk_platform)

        plat = Plataform(pygame.Rect(SPAWN, 300, 100,500), WALL2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+100, 550, 100,300), WALL2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+400, 450, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+500, 100, 100,450), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+590, 425, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)
        
        plat = Plataform(pygame.Rect(SPAWN+1000, 550, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+1200, 350, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+1300, 350, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+1400, 450, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+1500, 450, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)    

        wall = Plataform(pygame.Rect(SPAWN+1600, 250, 100,500), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+1700, 350, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+1800, 350, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)   

        wall = Plataform(pygame.Rect(SPAWN+1900, 150, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+2000, 550, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+2300, 450, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+2400, 450, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+2500, 400, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+2600, 450, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+2700, 450, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+2800, 550, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+3000, 400, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+3100, 350, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+3200, 300, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+3300, 300, 100,600), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+3400, 325, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+3800, 425, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+3400, 525, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+3800, 625, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+3900, 0, 100,425), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+3900, 550, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+4000, 600, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+4100, 600, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+4200, 600, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+4300, 500, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+5200, 550, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+5300, 550, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+5400, 450, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+5500, 450, 100,400), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(SPAWN+4950, 0 , 100,500), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+5050, 375, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+5400, 250, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+5050, 125, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+5400, 0, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(SPAWN+5600, 0 , 100,800), WALL2PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(SPAWN+5700, 100, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+5700, 300, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+5700, 500, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+6300, 150, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+6300, 380, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(SPAWN+6300, 550, 200,25), PLATFORM3PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        right_limit_platf = Plataform(pygame.Rect(7700+CHARACTER_SPAWN_WIDTH, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(right_limit_platf)
        self.entities.add(right_limit_platf)
        platform_list.append(right_limit_platf)

        # Group with all collision platforms
        self.all_platforms = pygame.sprite.Group()
        for x in itertools.product(platform_list):
            self.all_platforms.add(x)
        
        # Invisible platform to the left's spawn
        left_limit_platf = Plataform(pygame.Rect(-10+SPAWN, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(left_limit_platf)
        self.entities.add(left_limit_platf)
        platform_list.append(left_limit_platf)

        # Invisible platform to the bosse's right
        right_limit_platf = Plataform(pygame.Rect(7400+CHARACTER_SPAWN_WIDTH, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(right_limit_platf)
        self.entities.add(right_limit_platf)
        platform_list.append(right_limit_platf)
    
    def add_powerups(self):
        health_up = HealthUp(pygame.Rect(1000+SPAWN, 600, 40,40), self)
        health_up2 = HealthUp(pygame.Rect(3000+SPAWN, 600, 40,40), self)
        health_up3 = HealthUp(pygame.Rect(4000+SPAWN, 500, 40,40), self)
        health_up4 = HealthUp(pygame.Rect(5000+SPAWN, 600, 40,40), self)
        health_up5 = HealthUp(pygame.Rect(5500+SPAWN, 380, 40,40), self)

        self.powerups.add(health_up)
        self.powerups.add(health_up2)
        self.powerups.add(health_up3)
        self.powerups.add(health_up4)
        self.powerups.add(health_up5)

        self.entities.add(health_up)
        self.entities.add(health_up2)
        self.entities.add(health_up3)
        self.entities.add(health_up4)
        self.entities.add(health_up5)
        
        health_up = HealthUp(pygame.Rect(3500+SPAWN, 550, 40,40), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)

        health_up = HealthUp(pygame.Rect(5700+SPAWN, 200, 40,40), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)

        health_up = HealthUp(pygame.Rect(5700+SPAWN, 400, 40,40), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)

        health_up = HealthUp(pygame.Rect(5700+SPAWN, 550, 40,40), self)
        self.powerups.add(health_up)
        self.entities.add(health_up)

        more_damage = MoreDamage(pygame.Rect(SPAWN, 200, 40,40), self)
        self.powerups.add(more_damage)
        self.entities.add(more_damage)

        more_damage = MoreDamage(pygame.Rect(SPAWN+6300, 50, 40,40), self)
        self.powerups.add(more_damage)
        self.entities.add(more_damage)

        martina = MartinaBomb(pygame.Rect(SPAWN+4300, 300, 100,100), self)
        self.powerups.add(martina)
        self.entities.add(martina)

    def add_boss(self):
        # We add the final boss and its weapons
        boss_weapon1 = Weapon((self.player.rect.center),"left",*MACHINEGUNE, self,'bad')
        boss_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        boss_weapon3 = Weapon((self.player.rect.center),"left",*MACHINEGUNE, self,'bad')
        self.entities.add(boss_weapon1)
        self.entities.add(boss_weapon2)
        self.entities.add(boss_weapon3)
        self.boss_burns = (enemyBoss(500,(CHARACTER_SPAWN_WIDTH+7300,CHARACTER_SPAWN_HEIGHT ), self,boss_weapon1,boss_weapon2,boss_weapon3, BURNS, 125,200))
        self.enemy_group.add(self.boss_burns)
        self.entities.add(self.boss_burns)

    def update(self,direction):
        pygame.display.update()
        mixer.music.unpause()
        if not(mixer.music.get_busy()):
            # We change the music to a specific sound for Level3
            mixer.music.load('Music/king_of_the_hill.mp3')
            # Each sound can sound louder or lower, so we change its volume in every level
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)
        # Update the clock, we call this method once per frame and our game will never run at more than 50 fps
        self.time = CLOCK.tick_busy_loop(FPS)
        # We are on Level3
        if not(self.levelInit):
            # We update all the elements declared in this level
            self.player.update(self.player.desired_direction, self.time)
            self.weapon.update(self.player,self.time,0,0)
            self.enemy_group.update(self.time)
            self.bullet_group.update(self.time)
            self.camera.update(self.player)
            self.powerups.update(self.time)
            self.boss_burns.update(self.time)
            # Check our player's health
            if self.player.health < 1:
                self.game_over = True
                # If our player's dead, we can try the level again
                menuP = FailLevel(self.director, Level3(self.director, self.auxVolume))
                self.director.changeLevel(menuP) 
            # The level is passed if we kill the boss
            if self.boss_burns.life <= 0:
                self.director.changeLevel(GameCompleted(self.director, self.auxVolume))
        # We are in the previous screen to the Level3
        else:
            # Unload the currently loaded music to free up resources
            mixer.music.unload()

    def events(self,events):
        # We are on Level3
        if not(self.levelInit):
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
        # We are in the previous screen to the Level3
        else:
            for event in events:
                # We notify the director if we want to exit
                if event.type== KEYDOWN:
                    if event.key== K_ESCAPE:
                        self.director.stackLevel(self.menu)
                    elif event.key== pygame.QUIT:
                        self.director.exitGame()
                    elif event.key == K_SPACE:
                        self.background = Manager.loadImage("level3background.png")
                        self.levelInit = False

    def draw(self,screen):
        # We are on Level3
        if not(self.levelInit):
            # We draw all our sprites, stored in the group self.entities
            screen.fill(BLACK)
            screen.blit(self.background,[0,0])
            # We apply each element to the camera, so we can scroll
            for e in self.entities:
                screen.blit(e.image, self.camera.apply(e)) 
            super().draw(screen)
            pygame.display.flip()
        # We are in the previous screen to the Level3
        else:
            # Screen where we show the world's context before the start of Level3
            screen.fill(BLACK)
            screen.blit(self.background,[0,0])
            myfont=pygame.font.SysFont("Britannic Bold", 40)
            f = open(HISTORY3PATH, "r")
            i = 300
            nlabel=myfont.render("Entering Level 3: Secret Nuclear Plant", 1, (255, 255, 255))
            screen.blit(nlabel,(200,200))
            for line in f.readlines():
                i += 50
                history1Label=myfont.render(line[:-1],1,(255, 255, 255))
                screen.blit(history1Label,(200,i))

    
