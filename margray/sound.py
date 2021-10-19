import pygame

class Sound():
    def __init__(self,sound_path):
        self.sound = pygame.mixer.Sound(sound_path)
    def play(self,loops=0,maxtime=0,fade_ms=0):
        self.sound.play(loops=loops,maxtime=maxtime,fade_ms=fade_ms)
    def stop(self):
        self.sound.stop()
    def set_volume(self,volume):
        self.sound.set_volume(volume)    
    def fadeOut(self,time=None):
        if time:self.sound.fadeout(time)
        else:self.sound.fadeout()                
class Music():
    def __init__(self,music_path):
        self.music = pygame.mixer.music.load(music_path)
    def play(self):
        pygame.mixer.music.play()
    def set_volume(self,volume):
        pygame.mixer.music.set_volume(volume)    
    def stop(self):
        pygame.mixer.music.stop()
    def unload(self):
        pygame.mixer.music.unload()    
    def pause(self):
        pygame.mixer.music.pause()
    def unpause(self):
        pygame.mixer.music.unpause()                