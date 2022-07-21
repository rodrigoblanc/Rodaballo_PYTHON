# -*- encoding: utf-8 -*-

from pygame import mixer
from configs import *
from level import Level
from level1 import Level1
from manager import Manager


class ElementGUI:
    def __init__(self, screen, rectangle):
        self.screen= screen
        self.rect= rectangle

    def setPosition(self, position):
        (positionx, positiony) = position
        self.rect.left= positionx
        self.rect.bottom= positiony

    def positionInElement(self, position):
        (positionx, positiony) = position
        if(positionx>=self.rect.left) and (positionx<=self.rect.right) and (positiony>=self.rect.top) and (positiony<=self.rect.bottom):
            return True
        else:
            return False

    def draw(self):
        raise NotImplemented("Tiene que implementar el metodo draw.")
        
    def action(self):
        raise NotImplemented("Tiene que implementar el metodo action.")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# BUTTONS
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

class Button(ElementGUI):
    def __init__(self, screen, imageName, position, scale):
        # The button image is loaded
        self.imagen= Manager.loadImage(imageName)
        self.imagen= pygame.transform.scale(self.imagen, (scale, scale))
        # The method of the parent class is called with the rectangle
        ElementGUI.__init__(self, screen, self.imagen.get_rect())
        # The rectangle is placed in its position
        self.setPosition(position)
    def draw(self, screen):
        screen.blit(self.imagen, self.rect)

# -----------------------------------------------------------------------
# Buttons options menu screen
# -----------------------------------------------------------------------

class ControlsButton(Button):
    def __init__(self, screen):
        Button.__init__(self, screen, 'controls.png', (880,500), 500)
    def action(self):
        pass

class UpVolumeButton(Button):
    def __init__(self, screen):
        Button.__init__(self, screen, 'upVolume.png', (1000,500), 50)
    def action(self):
        self.screen.menu.changeVolumeUp()


class DownVolumeButton(Button):
    def __init__(self, screen):
        Button.__init__(self, screen, 'downVolume.png', (1050,505), 50)
    def action(self):
        self.screen.menu.changeVolumeDown()

class ReturnButton(Button):
    def __init__(self, screen):
        Button.__init__(self, screen, 'exit_btn.png', (980,560), 20)
    def action(self):
        self.screen.menu.returnMainMenu()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# TEXTS
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

class TextGUI(ElementGUI):
    def __init__(self, screen, font, color, text, position):
        # The text image is created
        self.imagen= font.render(text, True, color)
        # The method of the parent class is called with the rectangle
        ElementGUI.__init__(self, screen, self.imagen.get_rect())
        # The rectangle is placed in its position
        self.setPosition(position)
    def draw(self, screen):
        screen.blit(self.imagen, self.rect)

# -----------------------------------------------------------------------
# Text main menu
# -----------------------------------------------------------------------

class PlayText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el estor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'START GAME', (1010, 505))
    def action(self):
        self.screen.menu.runGame()

class OptionsText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el estor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'OPTIONS', (1010, 535))
    def action(self):
        self.screen.menu.showScreenOptions()

class ExitText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el estor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'EXIT', (1010, 565))
    def action(self):
        self.screen.menu.exitProgram()

# -----------------------------------------------------------------------
# Texto menú opciones
# -----------------------------------------------------------------------

class ControlsText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el gestor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'CONTROLS', (1010, 505))
    def action(self):
        self.screen.menu.showControls()

class VolumeText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el gestor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'VOLUME', (1010, 535))
    def action(self):
        self.screen.menu.changeVolume()

class ReturnText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el gestor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'RETURN', (1010, 565))
    def action(self):
        self.screen.menu.returnMainMenu()

class ReturnOptionsMenuText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el gestor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'RETURN', (1010, 565))
    def action(self):
        self.screen.menu.returnOptionsMenu()

class ChangeVolumeText(TextGUI):
    def __init__(self, screen):
        # La font la debería cargar el gestor de recursos
        font = pygame.font.Font(MENU_FONT, 26)
        TextGUI.__init__(self, screen, font, (44, 250, 31), 'Change volume', (1010, 450))
    def action(self):
        pass

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# Screens
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

class ScreenGUI:
    def __init__(self, menu, imageName):
        self.menu= menu
        # The background image is loaded
        self.imagen= Manager.loadImage(imageName)
        self.imagen= pygame.transform.scale(self.imagen, (WIDTH, HEIGHT))
        # Have a list of GUI elements
        self.elementsGUI= []

    def events(self, event_list):
        for event in event_list:
            if event.type== MOUSEBUTTONDOWN:
                self.elementoClic= None
                for elemento in self.elementsGUI:
                    if elemento.positionInElement(event.pos):
                        self.elementoClic= elemento
            if event.type== MOUSEBUTTONUP:
                for elemento in self.elementsGUI:
                    if elemento.positionInElement(event.pos):
                        if(elemento == self.elementoClic):
                            elemento.action()
    
    def draw(self, screen):
        # We first draw the background image
        screen.blit(self.imagen, self.imagen.get_rect())
        # Then the buttons
        for elemento in self.elementsGUI:
            elemento.draw(screen)

class StartScreenGUI(ScreenGUI):
    def __init__(self, menu):
        ScreenGUI.__init__(self, menu, 'ImagenMenuInicio.png')
        # We create the text and put it in the list
        textoJugar = PlayText(self)
        textoOpciones = OptionsText(self)
        textoSalir = ExitText(self)
        self.elementsGUI.append(textoJugar)
        self.elementsGUI.append(textoOpciones)
        self.elementsGUI.append(textoSalir)

class ScreenOptions(ScreenGUI):
    def __init__(self, menu):
        ScreenGUI.__init__(self, menu, 'ImagenMenuInicio.png')
        # We create the texts and put them in the list
        controlsText = ControlsText(self)
        volumeText = VolumeText(self)
        exitText = ReturnText(self)
        self.elementsGUI.append(controlsText)
        self.elementsGUI.append(volumeText)
        self.elementsGUI.append(exitText)

class ScreenControls(ScreenGUI):
    def __init__(self, menu):
        ScreenGUI.__init__(self, menu, 'ImagenMenuInicio.png')
        # We create control menu button + exit
        controlsButton = ControlsButton(self)
        self.elementsGUI.append(controlsButton)
        exitText = ReturnOptionsMenuText(self)
        self.elementsGUI.append(exitText)
        
class ScreenChangeVolume(ScreenGUI):
    def __init__(self, menu):
        ScreenGUI.__init__(self, menu, 'ImagenMenuInicio.png')
        # We create volume up and down buttons + output text
        upVolumeButton = UpVolumeButton(self)
        self.elementsGUI.append(upVolumeButton)
        downVolumeButton = DownVolumeButton(self)
        self.elementsGUI.append(downVolumeButton)
        exitText = ReturnOptionsMenuText(self)
        self.elementsGUI.append(exitText)
        changeVolumeText = ChangeVolumeText(self)
        self.elementsGUI.append(changeVolumeText)

class Menu(Level):
    def __init__(self, director):
        # We call the constructor of the parent class
        Level.__init__(self, director)
        # We create the list of screens
        self.screenList= []

        self.auxVolume = 0.2

        # We create the screens that we are going to have
        # and we put them in the list
        # 0 -> main menu screen
        self.screenList.append(StartScreenGUI(self))
        # 1 -> options screen
        self.screenList.append(ScreenOptions(self))
        # 2 -> show controls screen
        self.screenList.append(ScreenControls(self))
        # 3 -> change volume screen
        self.screenList.append(ScreenChangeVolume(self))
        
        # Which screen are we currently on
        self.showMainMenuScreen()
        self.FirstLevel = False

    def update(self, *args):
        # Check if the music stream is playing
        if not(mixer.music.get_busy()):
            # If not, play this level's song
            mixer.music.load('Music/fresh.mp3')
            pygame.mixer.music.set_volume(self.auxVolume)
            mixer.music.play(-1)

    def events(self, event_list):
        # We are on the main menu screen
        if not(self.FirstLevel):
            # Se mira si se quiere salir de esta escena
            for event in event_list:
                # Si se quiere salir, se le indica al director
                if event.type== KEYDOWN:
                    if event.key== K_ESCAPE:
                        self.exitProgram()
                elif event.type== pygame.QUIT:
                    self.director.exitGame()
            # Se pasa la lista de eventos a la pantalla actual
            self.screenList[self.currentScreen].events(event_list)
        # We want to start Level1
        else:  
            for event in event_list:  
                if event.type==KEYDOWN:
                    if event.key == K_SPACE:
                        self.FirstLevel = False
                        fase = Level1(self.director, self.auxVolume )
                        self.director.stackLevel(fase)
                    elif event.key== K_ESCAPE:
                        self.exitProgram()
                    elif event.type== pygame.QUIT:
                        self.director.exitGame()
    def draw(self, screen):
        # We are on the main menu screen
        if not(self.FirstLevel):
            self.screenList[self.currentScreen].draw(screen)
        # We want to start Level1
        else:
            # Screen where we show the world's context before the start of Level1
            screen.fill(BLACK)
            myfont=pygame.font.SysFont("Britannic Bold", 40)
            f = open(HISTORYPATH, "r")
            i = 300
            nlabel=myfont.render("Level 1: The Streets of Korea", 1, (255, 255, 255))
            screen.blit(nlabel,(200,200))
            for line in f.readlines():
                i += 50
                history1Label=myfont.render(line[:-1],1,(255, 255, 255))
                screen.blit(history1Label,(200,i))

    def exitProgram(self):
        self.director.exitGame()

    def runGame(self):
        self.FirstLevel = True

    def showMainMenuScreen(self):
        mixer.music.unload()
        mixer.music.load('Music/fresh.mp3')
        pygame.mixer.music.set_volume(self.auxVolume)
        mixer.music.play(-1)
        self.currentScreen = 0
    
    def changeVolumeUp(self):
        self.auxVolume += 0.1
        if(self.auxVolume > 1):
            self.auxVolume = 1
        pygame.mixer.music.set_volume(self.auxVolume)
    
    def changeVolumeDown(self):
        self.auxVolume -= 0.1
        if(self.auxVolume < 0):
            self.auxVolume = 0
        pygame.mixer.music.set_volume(self.auxVolume)

    def showScreenOptions(self):
        self.currentScreen = 1
    
    def showControls(self):
        self.currentScreen = 2
    
    def changeVolume(self):
        self.currentScreen = 3

    def returnMainMenu(self):
        self.currentScreen = 0
    
    def returnOptionsMenu(self):
        self.currentScreen = 1