# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:38 2018

@author: Leon
"""

class TrialFunctions:
    
    def getAnswer(self, keyTorF, stimulus):
        
        if (stimulus == True and keyTorF == True):
            self.antwort = 1
                         
        if (stimulus == False and keyTorF == True):
            self.antwort = 2
             
        if (stimulus == True and keyTorF == False):
            self.antwort = 3
             
        if (stimulus == False and keyTorF == False):
            self.antwort = 4
            
        return self.antwort    

##         
              