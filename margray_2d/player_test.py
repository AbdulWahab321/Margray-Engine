from .main import *

class PlayerTest():
    def __init__(self,x,y,image_path=None,width=50,height=70,mslf=None,floor_rect=None):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.mslf = Game()
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
    def get_rect(self):
        return self.player.get_rect()
    def disableMovement(self):
        self.movementDisabled = True
    def enableMovement(self):
        self.movementDisabled = False
    def get_sprite(self):
        return self.player   
    def moveUp(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.player.moveUp(velocity)
    def moveDown(self,velocity):
        self.yVelocity = velocity
        if not self.movementDisabled:self.player.moveDown(velocity)
    def moveRight(self,velocity):
        self.xVelocity = velocity
        if not self.movementDisabled:self.player.moveRight(velocity)
    def moveLeft(self,velocity):
        self.xVelocity= velocity
        if not self.movementDisabled:self.player.moveLeft(velocity)
    def collidingEdges(self):
        return self.player.collidingEdges()