from .main import *

class Player():
    def __init__(self,x,y,image_path=None,width=50,height=70,mslf=None,floor_rect=None):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.mslf = mslf
        self.x = x
        self.y = y
        self.floor_rect = floor_rect
        self.movementDisabled = False
        self.jumping = False
        self.starting = True
        self.velocity = 0
        self.player = self.mslf.image_sprite(image_path,x,y,(width,height))
    def jump(self,velocity=10):
        self.moveUp(velocity)
    def draw(self):
        if not self.mslf.quited:
            self.player.draw()    
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
    def get_rect(self):
        return self.player.get_rect()
    def disableMovement(self):
        self.movementDisabled = True
    def enableMovement(self):
        self.movementDisabled = False
    def moveUp(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.player.moveUp(velocity)
    def get_sprite(self):
        return self.player   
    def moveDown(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.player.moveDown(velocity)
    def moveRight(self,velocity):
        self.xVelocity = velocity
        if not self.movementDisabled:self.player.moveRight(velocity)
    def collidingEdges(self):
        return self.player.collidingEdges()
    def moveLeft(self,velocity):
        self.xVelocity= velocity
        if not self.movementDisabled:self.player.moveLeft(velocity)