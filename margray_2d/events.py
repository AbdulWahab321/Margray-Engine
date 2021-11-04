from .constants import *

class EventHandler:
    def __init__(self,event):
        self.event = event
        self.currentev = None
        for ev in self.event:
            self.currentev = ev           
    
    def event_type_is(self,event):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.currentev.type == event:
                    return True
        except AttributeError:
            pass                                 
    def key_is_down(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event_type_is(KEYDOWN):
                    return True
                else:
                    return False
        except AttributeError:
            pass                 
    def key_is_up(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event_type_is(KEYUP):
                    return True
        except AttributeError:
            pass                         
    def get_keys(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.key_is_down():
                    return self.currentev.key
        except AttributeError:
            pass                 
    def get_event_type(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                return self.currentev.type   
        except AttributeError:
            pass             
    def isEventQuit(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.currentev.type == QUIT:
                    return True
        except AttributeError:
            pass                 
    def enableAutoQuit(self,MargrayClass):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                
                if self.currentev.type == QUIT:
                    return MargrayClass.quit()
                
        except AttributeError:
            pass         
    def windowExited(self):
        try:
            if self.currentev and str(type(self.currentev)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.currentev.type == QUIT:return True
                else:return False
        except AttributeError:
            pass                            
    def isKey(self, key=Keys.KEY_W):
        mslf = self
        class Key():
            def __init__(self):
                self.event = mslf.currentev
                
            def pressed(self,check_with_key_up=False):
                    if mslf.key_is_down():
                        if self.event.key == key:
                            return True
                    elif check_with_key_up:
                        if mslf.key_is_up():
                            if self.event.key == key:
                                return False      
            def released(self):
                if mslf.key_is_up():
                    if self.event.key == key:
                        return True                   
                elif mslf.key_is_down():
                    if self.event.key == key:
                        return False
            def holded(self):
                return pygame.key.get_pressed()[key]              
        return Key()                