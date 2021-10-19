import pygame

class TransparentSprite:
    def __init__(self,position=(),size=(),mslf=()):
        x,y = position
        self.x = x
        
        self.y = y
        self.size = size
        self.mslf = mslf
        self.movementDisabled = False
    def draw(self):
        self.rect = pygame.Surface(self.size)
        self.rect.set_alpha(0)
        self.mslf.screen.blit(self.rect,(self.x,self.y))
        return self.rect    
    def get_rect(self):
        return self.rect.get_rect()                          
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
    def setX(self,xpos):
        self.x = xpos
    def setY(self,ypos):
        self.y = ypos
    def setPosition(self,position=()):
        x,y = position
        self.x = x
        self.y = y 
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
    def moveUp(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.y-=velocity
    def moveDown(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.y+=velocity
    def moveRight(self,velocity):
        self.xVelocity = velocity
        if not self.movementDisabled:self.x+=velocity
    def moveLeft(self,velocity):
        self.xVelocity= velocity
        if not self.movementDisabled:self.x-=velocity       
    def get_size(self):
        return (self.get_width(),self.get_height())
    def get_width(self):
        return self.rect.get_width()
    def shrink(self,by:int):
        self.setSize((self.get_width()//by,self.get_height()//by))    
    def get_height(self):
        return self.rect.get_height()                
    def setPosToCursorPos(self,x=True, y=True, center=False):
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