import pygame
from .events import Events

class Sprite:
    def __init__(self,color,position=(0,0),radius=20,width = 0, draw_top_right = None, draw_top_left = None, draw_bottom_left = None, draw_bottom_right = None,mslf=None):
        x,y = position
        self.x = x
        self.color = color
        self.y = y
        self.velocity = 0
        self.width = width
        self.radius = radius
        self.mslf = mslf
        self.gravityDisabled = False
        self.stopGravity = False
        self.destroyed = False
        self.movementDisabled = False
        self.cursor_pos_disabled = False
        self.draw_top_right = draw_top_right
        self.draw_top_left = draw_top_left
        self.draw_bottom_right = draw_bottom_right
        self.draw_bottom_left = draw_bottom_left
    def draw(self):
        if not self.mslf.quited:
            if self.destroyed == False:
                self.circle = pygame.draw.circle(self.mslf.screen,self.color,(self.x,self.y),self.radius,self.width,self.draw_top_right,self.draw_top_left,self.draw_bottom_left,self.draw_bottom_right)      
    def destroy(self):
        try:
            del self.circle
            self.destroyed = True
            del self
        except:
             pass              
    def collidingEdges(self):
        collidingEdges = ""
        if self.x <=0:
            collidingEdges = ("x","left")
        elif self.x >= self.mslf.get_width() - self.radius*2:
            collidingEdges = ("x","right")
        if self.y >= self.mslf.get_height() - self.radius*2:
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
    def get_circle(self):
        return self.circle     
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
    def get_radius(self):
        return self.radius
    def get_width(self):
        return self.width
    def shrink(self,by:int):
        self.setSize((self.get_width()//by,self.get_height()//by))    
    def breakGravity(self):
        self.gravityDisabled = True    
    def unbreakGravity(self):
        self.gravityDisabled = False              
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
    def mouseHovered(self):
        pos = pygame.mouse.get_pos()
        if self.circle.collidepoint(pos[0],pos[1]):
            return True                                      
        else:
            return False
    def mousePressedOver(self,event):
        from .constants import MOUSEBUTTONDOWN
        pos = pygame.mouse.get_pos()
        if self.circle.collidepoint(pos[0],pos[1]):
            if pygame.mouse.get_pressed():
                if Events(event).event_type_is(MOUSEBUTTONDOWN):
                    return True
            else:
                return False                        
        else:
            return False                        
    def setPosToCursorPos(self,x=True, y=True, center=False):
        if not self.cursor_pos_disabled and not self.mslf.quited:
            mx,my = pygame.mouse.get_pos()
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