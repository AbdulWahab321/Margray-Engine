import pygame
from . import constants

class Button():
    def __init__(self,x,y,image_path,size,hoveredCallback=None,pressedCallback=None,mslf=None):
        self.width = None
        self.height = None 

        self.hc = hoveredCallback
        self.pc = pressedCallback
        if size:
            self.width, self.height = size
        self.image = pygame.image.load(image_path)
        if size:
            self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()    
        self.rect.topleft = (x,y)
        self.mslf = mslf
    def convert_Alpha(self):
        self.image = self.image.convert_alpha()
    def set_colorkey(self,colorkey):
        self.image.set_colorkey(colorkey)
    def activateEvents(self,gameRunEvent):
        if not self.mslf.quited:
            pos = pygame.mouse.get_pos()
            
            if self.rect.collidepoint(pos[0],pos[1]):
                if self.hc:self.hc()
                if gameRunEvent.event_type_is(constants.MOUSEBUTTONDOWN):
                    if self.pc:self.pc()                         
    def draw(self):
        if not self.mslf.quited:                 
            self.mslf.screen.blit(self.image,(self.rect.x,self.rect.y))    