import pygame
from .constants import *
from .events import *
import sys
import os

class MargrayGameEngine:
    def __init__(self):
        pygame.init()
        self.do = []
        self.isRunning  = False
        self.bg         = (0,0,0)
        self.resolution = ()
        self.updated    = False
        self.manualBg   = False
        self.quited     = False
    def create_screen(self,resolution=(800,600),flags=0,depth = 0, display = 0, vsync = 0):
        if str(type(resolution)).replace("<class","").replace("'>","").replace("'","").strip().lower() =="tuple":
            self.resolution = resolution
        elif str(type(resolution)).replace("<class","").replace(">","").replace("'","").strip().lower() == "str":
            self.resolution = (int(resolution.lower().split("x")[0]),int(resolution.lower().split("x")[1]))
        elif str(type(resolution)).replace("<class","").replace(">","").replace("'","").strip().lower() == "int":
            self.resolution = (resolution,resolution)    
        else:
            raise ValueError("Invalid type of resolution string or tuple or and integer are only supported")        
        self.screen = pygame.display.set_mode(self.resolution,flags,depth,display,vsync)
        self.set_caption("Margray game window")
        self.set_icon(os.path.join(os.path.dirname(__file__),"icon.png"))
    def set_caption(self,title,iconTitle=None):
        if not iconTitle:self.get_display().set_caption(title)
        else:self.get_display().set_caption(title,iconTitle)
    def set_bgcolor(self,rgb=(0,0,0)):
        if not self.quited:
            self.manualBg = True
            self.bg = rgb
            self.screen.fill(self.bg)   
    def set_icon(self,path):
        path = pygame.transform.scale(pygame.image.load(path),(32,32))
        self.get_display().set_icon(path)
    def musicManager(self):
        from . import sound
        return sound         
    def get_size(self):
        if not self.quited:return self.screen.get_size()    
    def get_width(self):
        if not self.quited:
            size = self.get_size()
            return size[0]
    def get_height(self):
        if not self.quited:
            size = self.get_size()
            return size[1]
    def player(self,x, y, image_path=None,width=50, height=70, floor_rect=None):
        mslf = self
        from . import player
        try:
            return player.Player(x, y, image_path, width,height,mslf,floor_rect)
        except pygame.error:
            pass
    def transparent_sprite(self,position=(0,0),size=(100,100)):
        mslf = self
        from . import transparent_sprite
        return transparent_sprite.TransparentSprite(position,size,mslf)    
    def background_image(self,image_path):
        mslf = self
        from . import background
        return background.Background(image_path, mslf)
    def scrolling_bg(self,image_path):
        from . import scrolling_bg
        return scrolling_bg.ScrollingBG(image_path)
    def flip_display(self):
        return self.get_display().flip()
    def image_button(self, image_path, x=50, y=50, size=None, hoveredCallback=None, pressedCallback=None):
        mslf = self
        from . import imbutton
        return imbutton.Button(x,y,image_path,size,hoveredCallback,pressedCallback,mslf)    
    def sprite(self,color=(0,155,120),position=(0,0),size=(100,100)):
        mslf = self
        from . import _sprite
        return _sprite.Sprite(color,position,size,mslf)     
    def fps(self):   
        from . import fps
        return fps.FPS()    
    def create_button(self, text="Hello", position=(50,50), size=(150,50), font="Corbel", fontColor=(255,255,255), fontSize=25, bg_color=(10,10,10), hovered_bg_color=(15,15,15), pressed_callback=None, padding_Y=5, padding_X=25, hovered_callback=None):
        mslf = self         
        from . import button
        return button.Button(text, position , font, fontColor, fontSize, bg_color, hovered_bg_color, pressed_callback, size, padding_Y, padding_X,hovered_callback, mslf)                 
    def image_sprite(self,image_path,x,y,size=None):
        mslf = self
        from . import imsprite
        csprite = imsprite.Sprite(image_path,x,y,size,mslf)        
        return csprite
    def animated_sprite(self,image_paths=[],x=50,y=50,size=None,startingIndex=0):
        mslf = self
        from . import animated_sprite
        return animated_sprite.AnimatedSprite(image_paths,x,y,size,startingIndex,mslf) 
    def animated_text(self,textlist=[], duration=185, startingIndex=0, position=(50,50), font="Arial", fontSize=35, color="white", bg_color=None):
        mslf = self
        from . import animated_text
        return animated_text.AnimatedText(textlist,duration,startingIndex, position,font,fontSize,color,bg_color,mslf)
    def get_display(self):
        return pygame.display
    def scrolling_background(self,image_path,velocity=0.9):
        mslf = self
        from . import scrolling_bg
        return scrolling_bg.ScrollingBG(image_path,velocity,self)
    def quit(self):
        self.quited = True
        pygame.quit()
        sys.exit()   
    def text(self,text="", position=(10,10), font="Arial", fontSize=35, color="black", bg_color=None):
        mslf = self
        from . import text as txt
        return txt.Text(text.encode(),position,font,fontSize,color,bg_color,mslf)    
    def image(self,image_path,x=50,y=50,size=None):
        mslf = self
        from . import image
        return image.Image(x,y,image_path,size,mslf)
    def update(self):
        if not self.quited:
            return self.get_display().update()      
    def run(self):
        if not self.quited:
            if self.manualBg==False:self.screen.fill(self.bg)
            return pygame.event.get()
        else:
            return [QUIT,"Program exited"]