import pygame

class Text:
    def __init__(self,text,position,font,fontSize,color,bg_color=None,mslf = None):
        self.color = color
        self.bg_color = bg_color
        self.x,self.y = position
        self.ufont = font
        self.ufontSize = fontSize
        self.font = pygame.font.SysFont(font,fontSize)
        self.text = self.font.render(text , True , self.color, self.bg_color)    
        self.mslf = mslf
    def changeText(self,text):
        self.text = self.font.render(str(text) , True , self.color, self.bg_color) 
    def changeFont(self,font):
        self.font = pygame.font.SysFont(font,self.ufontSize)
    def changeFontSize(self,fontSize):
        self.font = pygame.font.SysFont(self.ufont,fontSize)       
    def changeColor(self,color):
        self.color = color
        self.text = self.font.render(self.text , True , self.color, self.bg_color) 
    def changeBgColor(self,bgcolor):
        self.bg_color = bgcolor
        self.text = self.font.render(self.text , True , self.color, self.bg_color)                 
    def display(self):
        self.mslf.screen.blit(self.text , (self.x, self.y))  