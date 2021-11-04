from . import imsprite

class ScrollingBG:
    def __init__(self,image_path,velocity,mslf):
        self.velocity = velocity
        self.mslf = mslf
        size = (self.mslf.get_width(),self.mslf.get_height())
        self.bgCenter = imsprite.Sprite(image_path,0,0,size,mslf=mslf)
        self.bgLeft = imsprite.Sprite(image_path,self.bgCenter.get_width()+5,0,size,mslf=mslf)
        self.bgRight = imsprite.Sprite(image_path,-self.bgCenter.get_width()-5,0,size,mslf=mslf)
        self.bgDown = imsprite.Sprite(image_path,0,self.bgCenter.get_height()-5,size,mslf=mslf)
        self.bgUp = imsprite.Sprite(image_path,0,-self.bgCenter.get_height()+5,size,mslf=mslf)
    def draw(self):
        self.bgDown.draw()
        self.bgUp.draw()
        self.bgCenter.draw()
        self.bgLeft.draw()
        self.bgRight.draw()    
    def moveUp(self):
        if self.bgUp.get_YPosition()//2 < self.mslf.get_height()//2:
            self.bgCenter.moveUp(self.velocity)
            self.bgUp.moveUp(self.velocity)
            self.bgDown.moveUp(self.velocity)
        else:
            self.bgUp.setY(self.bgDown.get_height())    
            