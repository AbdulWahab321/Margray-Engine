import pygame
from . import constants


class Button():
    def __init__(self,text, position, font, fontColor, fontSize, bg_color, hovered_bg_color, pressed_callback, size, padding_Y=5, padding_X=25,hovered_callback=None,mslf=None):
        self.color = fontColor
        self.hovered_bg_color = hovered_bg_color
        self.bg_color = bg_color
        self.width = size[0]
        self.height = size[1]
        self.x = position[0]
        self.y = position[1]
        self.hc = hovered_callback
        smallfont = pygame.font.SysFont(font,fontSize)
        self.text = smallfont.render(text , True , self.color)
        self.pc = pressed_callback
        self.fontSize = fontSize
        self.addX = padding_X
        self.addY = padding_Y
        self.mslf = mslf
    def activateEvents(self, event):
            if not self.mslf.quited:
                mslf = self.mslf
                width, height = self.width, self.height
                mouse = pygame.mouse.get_pos()
                screen = mslf.screen
                mslf.isRunning = True
                if event.event_type_is(constants.MOUSEBUTTONDOWN):
                    if self.x <= mouse[0] <= self.x+width and self.y <= mouse[1] <= self.y+height:
                        if self.pc:self.pc()

                if self.x <= mouse[0] <= self.x+width and self.y <= mouse[1] <= self.y+height:
                    pygame.draw.rect(screen,self.hovered_bg_color,[self.x,self.y,width,height])
                    if self.hc:self.hc()
                else:
                    pygame.draw.rect(screen,self.bg_color,[self.x,self.y,width,height])        
    def draw(self):
        if not self.mslf.quited:
            self.mslf.screen.blit(self.text , (self.x+self.fontSize//2, self.y+self.fontSize//2))