import pygame

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
    def setMaxFPS(self,fps):
        return self.clock.tick(fps)
    def getFPS(self):
        return self.clock.get_time()