import pygame 
from pygame.locals import *

# File where we store all the references to the pictures and sounds used in this game

# MENU FONT
MENU_FONT = "Menu/pixelated.ttf"

#FPS 
FPS = 50

#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)

#CLOCK
CLOCK = pygame.time.Clock()

#SCREEN SET MODE
WIDTH = 1280
HEIGHT = 720

#SPAWN
SPAWN = -10000

#GRAVITY
GRAVITY = 0.8

#MOVE UNITS
MOVEMENT = 0.65
JUMP_HEIGHT = -16

#CARACTER SIZE
CHARACTER_SPAWN_HEIGHT = 610
CHARACTER_SPAWN_WIDTH = 10+SPAWN
PLAYER = "kate.png"
ENEMY = "militar.png"

#PATHS 
SHOOTPATH = "sprites/disparo.png"
HISTORYPATH = "history/history.txt"
HISTORY2PATH = "history/history2.txt"
HISTORY3PATH = "history/history3.txt"
CARPATH = "destroyed_car.png"
PLATFORM1PATH = "ledge2.png"
PLATFORM2PATH = "ledge1.png"
PLATFORM3PATH = "ledge3.png"
WALLPATH = "Wall.png"
WALL1PATH = "Wall1.png"
WALL2PATH = "Wall2.png"

#WEAPONS   Number of bullets, dispersion, time between shots, time the bullet stays alive, damage, Weapon ID

#Enemy Weapons
HANDGUNE = [1,0.0,900,1000,1,2,100000]
SHOTGUNE = [5,0.5,3000,400,2,5,100000]
MACHINEGUNE = [1,0.5,200,600,1,3,100000]
#Our Weapons
SHOTGUN = [10,0.5,1000,300,4,5,30]
HANDGUN = [1,0.0,300,5000,0,10,100000]

HANDGUNSFX = 'pistol_packing_mama.mp3'
SHOOTGUNSFX = 'de_feria.mp3'
ACIDSFX = 'cuspe.mp3'
PLACEHOLDERSFX = 'shootitos.mp3'

# OBJECTS
HEART = "heart.png"
BULLET = "bala.png"
EMPTY_HEART = "empty_heart.png"
SHOTGUN_PNG = "shotgun.png"
MARTINA = "lata.png"


# BOSSES
KIM = "kim.png"
BUSH = "bush.png"
BURNS = "burns.png"