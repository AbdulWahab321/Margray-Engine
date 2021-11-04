import pygame
from .transparent_sprite import TransparentSprite as TS
from margray.constants import MOUSEBUTTONDOWN
from .events import EventHandler as Events

class Sprite:
    def __init__(self,image_path,x=50,y=50,size=None,mslf=None):
        self.image = pygame.image.load(image_path)
        if size:self.size = size
        else:self.size = self.image.get_size()
        self.x = x
        self.y = y
        self.mslf = mslf
        self.collideEdges = False
        self.cursor_pos_disabled = False
        self.movementDisabled = False
        self.stopGravity = False
        self.destroyed = False
        if self.size:
            self.rect = TS((self.x,self.y),self.size,mslf)
        else:
            self.rect = TS((self.x,self.y),self.image.get_size(),mslf)
        self.gravityDisabled = False
        self.velocity = 0 
    def collidingEdges(self):
        collidingEdges = ""
        if self.x <=0:
            collidingEdges = ("x","left")
        elif self.x >= self.mslf.get_width() - self.get_width():
            collidingEdges = ("x","right")
        if self.y >= self.mslf.get_height() - self.get_height():
            collidingEdges = ("y","bottom")
        elif self.y <= 0:
            collidingEdges = ("y","top")
        class Collision:
            def __init__(self,col):
                self.col = col
            def get_colliding_Edge(self):
                return self.col[1]
            def get_x_or_y(self):
                return self.col[0]
            def get(self):
                return self.col
            def isColliding(self):
                if self.col != "":
                    return True
                else:
                    return False
        return Collision(collidingEdges)  

    def isCollidingSprite(self,sprite):
        if not self.destroyed:
            rect1 = self
            rect2 = sprite
            if (rect1.x < rect2.x + rect2.get_width() and rect1.x + rect1.get_width() > rect2.x and rect1.y < rect2.y + rect2.get_height() and rect1.get_height() + rect1.y > rect2.y):
                return True        
            else:
                return False
        else:
            return False    
    def convert_Alpha(self, alpha):
        self.image.convert_alpha(alpha)
    def set_colorkey(self,colorkey):
        self.image.set_colorkey(colorkey)
    def addGravity(self,limit,gravityPower=1,velocityCap=5):
        if not self.gravityDisabled:
            if not self.mslf.quited:
                if self.y < limit:
                    self.velocity += gravityPower
                if self.y > limit:
                    self.y = limit
                if self.velocity > velocityCap:
                    self.velocity = velocityCap
                self.y += self.velocity                         
    def get_centerX(self):
        return self.get_rect().centerx  
    def get_centerY(self):
        return self.get_rect().centery
    def get_top(self):
        return self.get_rect().top
    def get_bottom(self):
        return self.get_rect().bottom                
    def draw(self):
        if not self.mslf.quited:
            if not self.destroyed:
                image = self.image
                mslf = self.mslf
                if self.size:
                    self.image = pygame.transform.scale(image,self.size)
                self.rect.setY(self.y)
                self.rect.setX(self.x) 
                self.rect.setSize(self.size)
                self.rect.draw()
                mslf.screen.blit(self.image,(self.rect.x, self.rect.y))
                
                if self.collideEdges:
                    if self.collideEdges.get("x") == True:
                        if self.x >= mslf.resolution[0]-self.get_width():
                            self.setX(mslf.resolution[0]-self.get_width())
                    if self.collideEdges.get("y") == True:
                        if self.y >= mslf.resolution[1]-self.get_height():
                            self.setX(mslf.resolution[1]-self.get_height())  
    def mouseHovered(self):
        pos = pygame.mouse.get_pos()
        if self.image.get_rect().collidepoint(pos[0],pos[1]):
            return True                                      
        else:
            return False         
    def mousePressedOver(self,event):
        pos = pygame.mouse.get_pos()
        if self.image.get_rect().collidepoint(pos[0],pos[1]):
            if pygame.mouse.get_pressed():
                if Events(event).event_type_is(MOUSEBUTTONDOWN):
                    return True
            else:
                return False
        else:
            return False                
    def setX(self,xpos):
        self.x = xpos
    def setY(self,ypos):
        self.y = ypos
    def setPosition(self,position=()):
        x,y = position
        self.x = x
        self.y = y 
    def destroy(self):
        try:
            self.destroy_rect()
        except:
            self.destroy_rect()    
        try:
            self.rect.destroy()
            del self.rect
            self.destroyed = True
            del self
        except:
            pass        
    def destroy_rect(self):
        self.rect.destroy()                 
    def get_rect(self):
        return self.rect.get_rect()   
    def get_position(self):
        return (self.x,self.y)
    def get_XPosition(self):
        return self.rect.x
    def get_YPosition(self):
        return self.rect.y                
    def setSize(self,size):    
        self.size = size  
        self.image = pygame.transform.scale(self.image,size)
    def disableMovement(self):
        self.movementDisabled = True
    def enableMovement(self):
        self.movementDisabled = False   
    def breakGravity(self):
        self.gravityDisabled = True    
    def unbreakGravity(self):
        self.gravityDisabled = False          
    def moveUp(self,velocity):
        if not self.movementDisabled:self.y-=velocity
    def moveDown(self,velocity):
        if not self.movementDisabled:self.y+=velocity
    def moveRight(self,velocity):
        if not self.movementDisabled:self.x+=velocity
    def moveLeft(self,velocity):
        if not self.movementDisabled:self.x-=velocity       
    def get_size(self):
        return (self.image.get_width(),self.image.get_height())
    def flip_x(self):
        self.image = pygame.transform.flip(self.image,True,False)
    def flip_y(self):
        self.image = pygame.transform.flip(self.image,False,True)
    def flip(self):
        self.image = pygame.transform.flip(self.image,True,True)        
    def get_width(self):
        return self.image.get_width()
    def shrink(self,by:int):
        self.setSize((self.get_width()/by,self.get_height()/by))    
    def get_height(self):
        return self.image.get_height()
    def setPosToCursorPos(self,x=True, y=True, center=True):
        if not self.cursor_pos_disabled:
            mx,my = pygame.mouse.get_pos()
            if self.size:
                width, height = self.size
            else:
                width, height = self.image.get_width(), self.image.get_height()    
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
    def enableSetPosToCursorPos(self):
        self.cursor_pos_disabled = False    