import pygame

class Time:
    def __init__(self):
        self.last = pygame.time.get_ticks()
        
    def cooldownFinished(self,cooldown=1000):
        now = pygame.time.get_ticks()
        if now - self.last >= cooldown:
            self.last = now
            return True
        else:
            return False    