import pygame
from .constants import MOUSEBUTTONDOWN
from .events import EventHandler as Events

class Image:
    def __init__(self,x,y,image_path,size, mslf):
        self._image = pygame.image.load(image_path) 
        self.size = size
        self.mslf = mslf
        self.x = x
        self.y = y
        self.cursor_pos_disabled = False
        if self.size:
            self._image = pygame.transform.scale(self._image,size)
    def draw(self):
        if self.size:
            self._image = pygame.transform.scale(self._image,self.size)        
        self.mslf.screen.blit(self._image,(self.x,self.y))
    def image(self):
        return self._image
    def getPosition(self):
        return (self.x,self.y)
    def setPosition(self, position):
        self.x = position[0]
        self.y = position[1]
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def get_width(self):
        return self._image.get_width()
    def get_height(self):
        return self._image.get_height()
    def get_size(self):
        return self._image.get_size()   
    def setSize(self, size):
        self.size = size
    def setWidth(self, width):
        self.size = (width, self.size[1])
    def setHeight(self, height):
        self.size = (self.size[0],height)    
    def mouseHovered(self):
        pos = pygame.mouse.get_pos()
        if self.image.get_rect().collidepoint(pos[0],pos[1]):
            return True                                      
        else:
            return False         
    def mousePressedOver(self,event):
        pos = pygame.mouse.get_pos()
        if self._image.get_rect().collidepoint(pos[0],pos[1]):
            if pygame.mouse.get_pressed():
                if Events(event).event_type_is(MOUSEBUTTONDOWN):
                    return True
            else:
                return False
        else:
            return False               
    def setPosToCursorPos(self,x=True, y=True, center=True):
        if not self.cursor_pos_disabled and not self.mslf.quited:
            mx,my = pygame.mouse.get_pos()
            if self.size:
                width, height = self.size
            else:
                width, height = self._image.get_width(), self._image.get_height()    
            if center:
                if x==True:
                    self.setX(mx-width/2)
                else:
                    _string = str(x)
                    if _string.isnumeric():self.setX(x)    
                if y==True:
                    self.setY(my-height/2)   
                else:
                    _string = str(y)
                    self.setY(y)     
            else:
                if x==True:
                    self.setX(mx)
                else:
                    _string = str(x)
                    if _string.isnumeric():self.setX(x)    
                if y==True:
                    self.setY(my)
                else:
                    _string = str(y)
                    self.setY(y)                              
    def disableSetPosToCursorPos(self):
        self.cursor_pos_disabled = True                               