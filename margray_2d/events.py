from .constants import *

class EventHandler:
    def __init__(self,event):
        self.event = event
    def event_type_is(self,event):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.type == event:
                    return True
        except AttributeError:
            pass                 
    def event_key_is(self,key):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.key == key:
                    return True  
        except AttributeError:
            pass                        
    def key_is_down(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.type == KEYDOWN:
                    return True
                else:
                    return False
        except AttributeError:
            pass                 
    def key_is_up(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.type == KEYUP:
                    return True
        except AttributeError:
            pass                         
    def get_keys(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.key_is_down():
                    return self.event.key
        except AttributeError:
            pass                 
    def get_event_type(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                return self.event.type   
        except AttributeError:
            pass             
    def isEventQuit(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.key == QUIT:
                    return True
        except AttributeError:
            pass                 
    def enableAutoQuit(self,MargrayClass):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                
                if self.event.type == QUIT:
                    return MargrayClass.quit()
                
        except AttributeError:
            pass         
    def windowExited(self):
        try:
            if str(type(self.event)).replace("<class","").replace("'>","").replace("'","").strip() !="int":
                if self.event.type == QUIT:return True
                else:return False
        except AttributeError:
            pass                            
    def isKey(self, key=Keys.KEY_W):
        mslf = self
        class Key():
            def __init__(self):
                self.event = mslf.event
            def pressed(self,check_with_key_up=False):
                    if mslf.key_is_down():
                        if self.event.key == key:
                            return True
                        else:
                            return False
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
                          
        return Key()                