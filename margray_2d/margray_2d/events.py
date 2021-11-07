from .constants import *
from .time import Time

class EventHandler:
    def __init__(self,event):
        self.event = event
        self.currentev = None
         
    def event_type_is(self,event):
        try:
            for currentev in self.event:
                if currentev:
                    if currentev.type == event:
                        return True
        except AttributeError:
            pass                                 
    def key_is_down(self):
        try:
            for currentev in self.event:
                if currentev:
                    if self.event_type_is(KEYDOWN):
                        return True
                    else:
                        return False
        except AttributeError:
            pass                 
    def key_is_up(self):
        try:
            for currentev in self.event:
                if currentev:
                    if self.event_type_is(KEYUP):
                        return True
        except AttributeError:
            pass                         
    def get_keys(self):
        try:
            for currentev in self.event:
                if currentev:
                    if self.key_is_down():
                        return self.currentev.key
        except AttributeError:
            pass                 
    def get_event_type(self):
        try:
            for currentev in self.event:
                if currentev:
                    return currentev.type   
        except AttributeError:
            pass             
    def isEventQuit(self):
        try:
            for currentev in self.event:
                if currentev:
                    if currentev.type == QUIT:
                        return True
        except AttributeError:
            pass                 
    def enableAutoQuit(self,MargrayClass):
        try:
            for currentev in self.event:
                if currentev:  
                    if currentev.type == QUIT:
                        return MargrayClass.quit()
                
        except AttributeError:
            pass         
    def windowExited(self):
        try:
            for currentev in self.event:
                if currentev:
                    if currentev.type == QUIT:return True
                    else:return False
        except AttributeError:
            pass                            
    def isKey(self, key=Keys.KEY_W):
        mslf = self
        class Key():
            def __init__(self):
                pass                
            def pressed(self,check_with_key_up=False):
                for currentev in mslf.event:
                    if currentev:
                        if mslf.key_is_down():
                            if currentev.key == key:
                                return True
                        elif check_with_key_up:
                            if mslf.key_is_up():
                                if currentev.key == key:
                                    return False      
            def released(self):
                for currentev in mslf.event:
                    if currentev:                
                        if mslf.key_is_up():
                            if currentev.key == key:
                                return True                   
                        elif mslf.key_is_down():
                            if currentev.key == key:
                                return False
            def held(self):
                return pygame.key.get_pressed()[key]   
            def held_for(self,timeClass:Time,milliseconds):
                if pygame.key.get_pressed()[key]:
                    if timeClass.cooldownFinished(milliseconds) and pygame.key.get_pressed()[key]:
                        return True 
                    else:
                        return False                  
        return Key()                