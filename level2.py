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
from level3 import *
from levelpass import *

class Level2(Level):
    def __init__(self,director, auxVolume) :
        super().__init__(director)
        # Each level will have its own song and volume
        self.auxVolume = auxVolume
        mixer.music.unload()
        mixer.music.load('Music/atf.mp3')
        mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.auxVolume)
        # We manage the sounds with our resource manager
        Manager.loadSound(SHOOTGUNSFX).set_volume(self.auxVolume)
        Manager.loadSound(HANDGUNSFX).set_volume(self.auxVolume)
        # levelInit allows us to know when the level2 starts
        # = true -> screen showing the context of the story previous to the level
        # = false -> level2 starts
        self.levelInit = True
        self.player = MainCharacter((CHARACTER_SPAWN_WIDTH,CHARACTER_SPAWN_HEIGHT), self)
        total_level_width  = 600*32 # calculate size of level in pixels
        total_level_height = 400*32
        # Custom camera for scroll
        self.camera = CustomCamera(total_level_width, total_level_height)
        self.time = CLOCK.tick_busy_loop(FPS)
        self.menu = LevelMenu(director)
        self.screen = director.screen
        self.game_over = False
        self.background = Manager.loadImage("ViajeCoreaEEUU.png")
        
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
        self.add_enemies()
        self.add_platforms()
        self.add_powerups()
        self.add_boss()

    def add_enemies(self):

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux = (enemyShotgun(10,(CHARACTER_SPAWN_WIDTH+900,CHARACTER_SPAWN_HEIGHT ), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux)
        self.entities.add(enemy_aux)


        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+1000,CHARACTER_SPAWN_HEIGHT), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+1450,CHARACTER_SPAWN_HEIGHT), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(10,(CHARACTER_SPAWN_WIDTH+1600,CHARACTER_SPAWN_HEIGHT-200), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2000,CHARACTER_SPAWN_HEIGHT), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+2500,CHARACTER_SPAWN_HEIGHT), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        self.entities.add(enemy_weapon2)
        enemy_aux2 = (enemyShotgun(10,(CHARACTER_SPAWN_WIDTH+3200,CHARACTER_SPAWN_HEIGHT-400), self,enemy_weapon2))
        self.enemy_group.add(enemy_aux2)
        self.entities.add(enemy_aux2)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+3100,CHARACTER_SPAWN_HEIGHT-300), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+3700,CHARACTER_SPAWN_HEIGHT-300), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)

        enemy_weapon1 = Weapon((self.player.rect.center),"left",*HANDGUNE, self,'bad')
        self.entities.add(enemy_weapon1)
        enemy_aux1 = (enemyBasic(10,(CHARACTER_SPAWN_WIDTH+4200,CHARACTER_SPAWN_HEIGHT-300), self,enemy_weapon1))
        self.enemy_group.add(enemy_aux1)
        self.entities.add(enemy_aux1)


    def add_platforms(self):
        # Grupo con plataforma base: acera
        sidewalk_platform = Plataform(pygame.Rect(SPAWN, 700, 50000, 50), "empty", self)
        
        self.platform.add(sidewalk_platform)
        self.entities.add(sidewalk_platform)
        
        self.entities.add(self.bullet_group)
        self.weapon = Weapon((self.player.rect.center),"left",*HANDGUN, self,'good')
        self.entities.add(self.weapon)

        platform_list = []
        platform_list.append(sidewalk_platform)

        plat = Plataform(pygame.Rect(400+SPAWN, 550, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(600+SPAWN, 500, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(1000+SPAWN, 550, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(1200+SPAWN, 400, 100,400), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(1600+SPAWN, 550, 100,400), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(1800+SPAWN, 500, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(2200+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(2800+SPAWN, 550, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(3000+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(3100+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(3200+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        wall = Plataform(pygame.Rect(3300+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(3400+SPAWN, 425, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(3600+SPAWN, 575, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        wall = Plataform(pygame.Rect(3800+SPAWN, 400, 100,500), WALL1PATH, self)
        self.spriteGroup.add(wall)
        self.entities.add(wall)
        platform_list.append(wall)

        plat = Plataform(pygame.Rect(3900+SPAWN, 500, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(4300+SPAWN, 625, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

        plat = Plataform(pygame.Rect(4500+SPAWN, 550, 200,25), PLATFORM2PATH, self)
        self.spriteGroup.add(plat)
        self.entities.add(plat)
        platform_list.append(plat)

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
        right_limit_platf = Plataform(pygame.Rect(5150+CHARACTER_SPAWN_WIDTH, 0, 20, 2000), "empty", self)
        self.spriteGroup.add(right_limit_platf)
        self.entities.add(right_limit_platf)
        platform_list.append(right_limit_platf)

    def add_powerups(self):
        health_up = HealthUp(pygame.Rect(1000+SPAWN, 600, 40,40), self)
        health_up2 = HealthUp(pygame.Rect(1680+SPAWN, 600, 40,40), self)
        health_up3 = HealthUp(pygame.Rect(2010+SPAWN, 600, 40,40), self)
        health_up4 = HealthUp(pygame.Rect(2800+SPAWN, 600, 40,40), self)
        health_up5 = HealthUp(pygame.Rect(3700+SPAWN, 600, 40,40), self)
        more_damage = MoreDamage(pygame.Rect(1300+SPAWN, 600, 40,40), self)

        self.powerups.add(health_up)
        self.powerups.add(health_up2)
        self.powerups.add(health_up3)
        self.powerups.add(health_up4)
        self.powerups.add(health_up5)
        self.powerups.add(more_damage)

        self.entities.add(health_up)
        self.entities.add(health_up2)
        self.entities.add(health_up3)
        self.entities.add(health_up4)
        self.entities.add(health_up5)
        self.entities.add(more_damage)

    def add_boss(self):
        # We add the final boss and its weapons
        boss_weapon1 = Weapon((self.player.rect.center),"left",*MACHINEGUNE, self,'bad')
        boss_weapon2 = Weapon((self.player.rect.center),"left",*SHOTGUNE, self,'bad')
        boss_weapon3 = Weapon((self.player.rect.center),"left",*MACHINEGUNE, self,'bad')
        self.entities.add(boss_weapon1)
        self.entities.add(boss_weapon2)
        self.entities.add(boss_weapon3)
        self.boss_bush = (enemyBoss(150,(CHARACTER_SPAWN_WIDTH+5000,CHARACTER_SPAWN_HEIGHT ), self,boss_weapon1,boss_weapon2,boss_weapon3, BUSH, 100, 200))
        self.enemy_group.add(self.boss_bush)
        self.entities.add(self.boss_bush)

    def update(self,direction):
        pygame.display.update()
        mixer.music.unpause()
        if not(mixer.music.get_busy()):
            # We change the music to a specific sound for Level2
            mixer.music.load('Music/atf.mp3')
            # Each sound can sound louder or lower, so we change its volume in every level
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)
        # Update the clock, we call this method once per frame and our game will never run at more than 50 fps
        self.time = CLOCK.tick_busy_loop(FPS)
        # We are on Level2
        if not(self.levelInit):
            # We update all the elements declared in this level
            self.player.update(self.player.desired_direction, self.time)
            self.weapon.update(self.player,self.time,0,0)
            self.enemy_group.update(self.time)
            self.bullet_group.update(self.time)
            self.camera.update(self.player)
            self.powerups.update(self.time)
            self.boss_bush.update(self.time)
            # Check our player's health
            if self.player.health < 1:
                self.game_over = True
                # If our player's dead, we can try the level again
                menuP = FailLevel(self.director, Level2(self.director, self.auxVolume))
                self.director.changeLevel(menuP)
            # The level is passed if we kill the boss
            if self.boss_bush.life <= 0:
                self.director.changeLevel(LevelPass(self.director, Level3(self.director, self.auxVolume), self.auxVolume))
        # We are in the previous screen to the Level2
        else:
            # Unload the currently loaded music to free up resources
            mixer.music.unload()


    def events(self,events):
        # We are on Level2
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
        # We are in the previous screen to the Level2
        else:
            for event in events:
                # We notify the director if we want to exit
                if event.type== KEYDOWN:
                    if event.key== K_ESCAPE:
                        self.director.stackLevel(self.menu)
                    elif event.key== pygame.QUIT:
                        self.director.exitGame()
                    elif event.key == K_SPACE:
                        self.background = Manager.loadImage("Casablanca.png")
                        self.levelInit = False

    def draw(self,screen):
        # We are on Level2
        if not(self.levelInit):
            # We draw all our sprites, stored in the group self.entities
            screen.fill(BLACK)
            screen.blit(self.background,[0,0])
            # We apply each element to the camera, so we can scroll
            for e in self.entities:
                screen.blit(e.image, self.camera.apply(e)) 
            super().draw(screen)
            pygame.display.flip()
        # We are in the previous screen to the Level2
        else:
            # Screen where we show the world's context before the start of Level2
            screen.fill(BLACK)
            screen.blit(self.background,[0,0])
            myfont=pygame.font.SysFont("Britannic Bold", 40)
            f = open(HISTORY2PATH, "r")
            i = 300
            nlabel=myfont.render("Entering Level 2: The White House", 1, (255, 255, 255))
            screen.blit(nlabel,(200,200))
            for line in f.readlines():
                i += 50
                history1Label=myfont.render(line[:-1],1,(255, 255, 255))
                screen.blit(history1Label,(200,i))