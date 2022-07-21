# -*- coding: utf-8 -*-

import pygame, os
from pygame.locals import *
pygame.mixer.init()

# In this case it is implemented as an empty class, with only class methods
class Manager(object):
    resources = {}
            
    @classmethod
    def loadImage(cls, name):
        # If the filename is among the resources already loaded
        if name in cls.resources:
            # That resource is returned
            return cls.resources[name]
        # If it has not been uploaded before
        else:
            # The image is loaded indicating the folder in which it is
            fullname = os.path.join('sprites', name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error as message:
                print ('Cannot load image:', fullname)
                raise SystemExit
            # It is stored
            cls.resources[name] = image
            # It is returned
            return image
    @classmethod
    def loadImageScaled(cls, name, x, y):
        # If the filename is among the resources already loaded
        if name in cls.resources:
            # That resource is returned
            return cls.resources[name]
        # If it has not been uploaded before
        else:
            # The image is loaded indicating the folder in which it is
            fullname = os.path.join('sprites', name)
            try:
                image = pygame.image.load(fullname)
                image = pygame.transform.scale(image, (x,y))
            except pygame.error as message:
                print ('Cannot load image:', fullname)
                raise SystemExit
            # It is stored
            cls.resources[name] = image
            # It is returned
            return image

    @classmethod
    def CargarArchivoCoordenadas(cls, name):
        # If the filename is among the resources already loaded
        if name in cls.resources:
            # That resource is returned
            return cls.resources[name]
        # If it has not been uploaded before
        else:
            # The resource is loaded indicating the name of its folder
            fullname = os.path.join('imagenes', name)
            pfile=open(fullname,'r')
            datos=pfile.read()
            pfile.close()
            # It is stored
            cls.resources[name] = datos
            # It is returned
            return datos

    @classmethod
    def loadSound(cls,name):
        # If the filename is among the resources already loaded
        if name in cls.resources:
            # That resource is returned
            return cls.resources[name]
        # If it has not been uploaded before
        else :
            # The resource is loaded indicating the name of its folder
            fullname = os.path.join('sfx',name)
            music = pygame.mixer.Sound(fullname)
            music.set_volume(0.2)
            # It is stored
            cls.resources[name] = music
            # It is returned
            return music

