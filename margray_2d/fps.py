import pygame

class FPS:
    def __init__(self,mslf):
        self.mslf = mslf
        self.clock = pygame.time.Clock()
    def setMaxFPS(self,fps):
        self.mslf.frameRateSet = True
        return self.clock.tick(fps)
    def getFPS(self):
        return self.clock.get_fps()
    