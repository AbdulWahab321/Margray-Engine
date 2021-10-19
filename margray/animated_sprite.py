import pygame
from .time import Time
from .constants import MOUSEBUTTONDOWN
from .events import Events


class AnimatedSprite:
    def __init__(self,image_path,x,y,size=None,startingIndex=0,mslf = None):
        self.images = []        
        for i in image_path: 
            image = pygame.image.load(i)
            self.images.append(image)
        self.size = size
        self.x = x
        self.y = y
        self.images2 = []
        self.startingIndex = startingIndex
        self.index = startingIndex
        self.mslf = mslf
        self.collideEdges = False
        self.cursor_pos_disabled = False
        self.movementDisabled = False
        self.stopGravity = False
        self.destroyed = False
        self._stopAnimation = False
        self.timeClass = Time()
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
    def appendImage(self,image_path):
        image = pygame.image.load(image_path)
        self.images.append(image)
    def setImages(self,image_paths=[]):
        for i in image_paths: 
            image = pygame.image.load(i)
            self.images.append(image)
    def replaceImageOnIndex(self,index,image_path):
        self.images.pop(index)
        image = pygame.image.load(image_path) 
        self.images.insert(index,image)
    def setCurrentIndex(self,index):
        self.index = index       
    def pauseAnimation(self,image_index=None):
        if image_index:self.index = image_index
        self._stopAnimation = True     
    def resumeAnimation(self):
        self._stopAnimation = False
    def getCurrentImage(self):
        return self.current_image      
    def collideRect(self,rect,ground_y=None):
        ypos = self.get_rect().y
        y = None
        if ground_y:y = ground_y
        else:y = self.mslf.get_height() - self.get_height()
        
        if ypos >= y:  
            self.get_rect().y = ground_y 
    def convert_Alpha(self, alpha):
        self.image.convert_alpha(alpha)
    def set_colorkey(self,colorkey):
        self.image.set_colorkey(colorkey)
    def addGravity(self,limit=None,gravityPower=1,velocityCap=5):
        if limit == None:
            limit = self.mslf.get_height() - self.get_height()    
        else:
            limit = limit    
        if not self.gravityDisabled:
            if not self.mslf.quited:
                if self.y < limit:
                    self.velocity += gravityPower
                if self.y > limit:
                    self.y = limit
                if self.velocity > velocityCap:
                    self.velocity = velocityCap
                self.y += self.velocity                         
    def draw(self):
        if not self.mslf.quited:
            if not self.destroyed:
                self.current_image = self.images[self.index]
                image = self.images[self.index]
                mslf = self.mslf
                if self.size:
                    self.image = pygame.transform.scale(image,self.size)
                else:
                    self.image = image    
                mslf.screen.blit(self.image,(self.x, self.y))
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
    def insertImageBeforeIndex(self,index=1,image_path=""):
        image = pygame.image.load(image_path)
        self.images.insert(index,image)
    def getCurrentIndex(self):
        return self.index        
    def animate(self,duration=185):
        self.frameRate = duration
        if not self._stopAnimation:
            if self.timeClass.cooldownFinished(self.frameRate):
                if len(self.images) > self.index:
                    self.index+=1
                if len(self.images) == self.index:
                    self.index = self.startingIndex         
    def incrementIndex(self):
        if len(self.images) > self.index:
            self.index+=1
        if len(self.images) == self.index:
            self.index = self.startingIndex                                
    def setFrameRate(self, frameRate):
        self.frameRate = frameRate
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
            self.destroyed = True
            del self
        except:
            pass                     
    def get_rect(self):
        return self.image.get_rect()    
    def get_position(self):
        return (self.x,self.y)
    def get_XPosition(self):
        return self.x
    def get_YPosition(self):
        return self.y                
    def setSize(self,size):    
        self.size = size  
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
        return self.size[0]
    def shrink(self,by:int):
        self.setSize((self.get_width()//by,self.get_height()//by))    
    def get_height(self):
        return self.size[1]
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