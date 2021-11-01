from .text import Text
from .time import Time
from . import constants

class AnimatedText:
    def __init__(self,textlist,duration,startingIndex,position,font,fontSize,color,bg_color=None,mslf = None):
        self.index = 0
        self.totalLoops = 0
        self.textlist = textlist
        self.text = self.textlist[self.index]
        self.position = position
        self.textClass = Text(self.text,self.position,font,fontSize,color,bg_color,mslf)
        self.timeClass = Time()
        self.duration = duration
        self._stopAnimation = False
        self.startingIndex = startingIndex
    def display(self):
        self.textClass.display()
    def changeFont(self,font):
        self.textClass.changeFont(font)
    def changeColor(self,color):
        self.textClass.changeColor(color)
    def chnageBgColor(self,bg_color):
        self.textClass.changeBgColor(bg_color)
    def changeFontSize(self,fontSize):    
        self.textClass.changeFontSize(fontSize)           
    def animate(self,loops="infinite",stoppingIndex:str|int="last"):
        if not self._stopAnimation:
            if loops == "infinite":
                if self.timeClass.cooldownFinished(self.duration):
                    if self.index != len(self.textlist)-1:
                        self.index+=1
                        self.text = self.textlist[self.index]
                        self.textClass.changeText(self.text)
                    else:
                        self.index = self.startingIndex 
                        self.text = self.textlist[self.index]
                        self.textClass.changeText(self.text)           
            else:
                if self.timeClass.cooldownFinished(self.duration):
                    if not self.totalLoops == loops:
                        if self.index != len(self.textlist)-1:
                            self.index+=1
                            self.text = self.textlist[self.index]
                            self.textClass.changeText(self.text)
                        else:
                            self.totalLoops+=1
                            self.index = self.startingIndex 
                            self.text = self.textlist[len(self.textlist)-1 if stoppingIndex=="last" else stoppingIndex]
                            self.textClass.changeText(self.text)       
                    else:
                        self.text = self.textlist[len(self.textlist)-1 if stoppingIndex=="last" else stoppingIndex]
                        self.textClass.changeText(self.text)                     
    def replaceTextOnIndex(self,index,text):
        self.textlist.pop(index)
        self.textlist.insert(index,text)                     
    def changeDuration(self, duration):
        self.duration = duration
    def incrementIndex(self):
        if len(self.textlist) > self.index:
            self.index+=1
            self.text = self.textlist[self.index]
            self.textClass.changeText(self.text)             
        if len(self.textlist) == self.index:
            self.index = self.startingIndex 
            self.text = self.textlist[self.index]
            self.textClass.changeText(self.text)                
    def setTextList(self, textList=[]):
        if len(textList) != 0:
            self.textlist = textList
            self.text = self.textlist[self.index]
            self.textClass.changeText(self.text)                 
    def pauseAnimation(self,stop_on_index=None):
        if stop_on_index:self.index = stop_on_index
        self._stopAnimation = True     
    def resumeAnimation(self):
        self._stopAnimation = False                              
    def appendText(self,text):
        self.textlist.append(text)            
    def getCurrentText(self):
        return self.text
    def setCurrentIndex(self,index):
        self.index = index