import pygame
class Background:
    def __init__(self, image_path, optionalSize, mslf):
        self.mslf = mslf
        self.image = pygame.image.load(image_path)
        self.opsize = optionalSize
        self.x = 0
        self.y = 0
    def setBackground(self):  
        if not self.mslf.quited:  
            image = pygame.transform.scale(self.image,self.mslf.get_size() if not self.opsize else self.opsize)
            self.mslf.screen.blit(image,(self.x,self.y))