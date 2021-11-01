class SpriteGroup():
    def __init__(self):
        self.sprites = []
        self.lenght = 0
    def addSprite(self, sprite):
        self.sprites.append(sprite)
        self.lenght = len(self.sprites)
    def addSprites(self, spritesList):
        for sprite in spritesList:
            self.sprites.append(sprite)
            self.lenght = len(self.sprites)
    def remove(self, sprite):
        if self.lenght!=0:
            if sprite in self.sprites:
                self.sprites.remove(sprite)
                self.lenght = len(self.sprites)
            else:
                raise ValueError("Specified sprite is not added to the Group")        
    def moveUp(self,velocity):
        if self.lenght!=0:
            for sprite in self.sprites:
                sprite.yVelocity = velocity
                if not sprite.movementDisabled:sprite.moveUp(velocity)
    def moveDown(self,velocity):
        if self.lenght!=0:
            for sprite in self.sprites:
                sprite.yVelocity = velocity
                if not sprite.movementDisabled:sprite.moveDown(velocity)
    def moveRight(self,velocity):
        if self.lenght!=0:
            for sprite in self.sprites:
                sprite.xVelocity = velocity
                if not sprite.movementDisabled:sprite.x+=velocity
    def moveLeft(self,velocity):
        if self.lenght!=0:
            for sprite in self.sprites:
                sprite.xVelocity = velocity
                if not sprite.movementDisabled:sprite.x-=velocity    
    def isTouching(self,sprite):
        if self.lenght!=0:
            for csprite in self.sprites:
                if csprite.isCollidingSprite(sprite):
                    return True
    def isTouchingGroup(self,group,killGroup1=False,killGroup2=False):
        if self.lenght!=0:
            for csprite in self.sprites:
                for sprite in group.sprites:
                    if csprite.isCollidingSprite(sprite):
                        if killGroup1:
                            self.sprites = []
                        if killGroup2:
                            group.sprites = []    
                        return True                
                
    def getTouchingSprite(self, target_sprite,callbacks=None):
        if self.lenght!=0:
            for csprite in self.sprites:
                if csprite.isCollidingSprite(target_sprite):
                    if callbacks:callbacks()
                    return csprite 
    def getTouchingSpritesFromGroup(self, target_group,callbacks=None):
        if self.lenght!=0:
            for csprite in self.sprites:
                for target_sprite in target_group.sprites:
                    if csprite.isCollidingSprite(target_sprite):
                        if callbacks:callbacks()
                        return (csprite,target_sprite)                 
    def drawAll(self):
        if self.lenght!=0:
            for sprite in self.sprites:
                sprite.draw()  
    def setSize(self, size):
        if self.lenght!=0:
            for sprite in self.sprites:
                if hasattr(sprite, 'circle'):
                    if str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "tuple":
                        sprite.setSize(size[0])
                    elif str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "int":
                        sprite.setSize(size)
                    elif str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "str":        
                        sprite.setSize(int(size))
                else:
                    if str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "tuple":
                        sprite.setSize(size)
                    elif str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "int":
                        sprite.setSize(size,size)
                    elif str(type(size)).replace("<class","").replace("'>","").replace("'","").strip().lower() == "str":        
                        try:    
                            sprite.setSize(int(size.split("x")[0]),int(size.split("x")[1]))       
                        except IndexError:
                            sprite.setSize(size)
    def destroyAll(self): 
        if self.lenght!=0:
            for sprite in self.sprites:
                try:
                    sprite.destroy()
                except:
                    pass     