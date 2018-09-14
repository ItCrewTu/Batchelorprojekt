# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:38 2018

@author: Leon
"""




class TrialFunctions:
    #L evaluate yes/no task
    def getAnswerYesNo(self, keyTorF, stimulus):
        ##Hit
        if (stimulus == True and keyTorF == True):
            self.antwort = 1
        ##False Alarm
        if (stimulus == False and keyTorF == True):
            self.antwort = 2
        ##Correct Rejection
        if (stimulus == False and keyTorF == False):
            self.antwort = 3
        ##Miss
        if (stimulus == True and keyTorF == False):
            self.antwort = 4

        return self.antwort
    #L evaluate 2 IFC task
    def getAnswer2IFC (self, key1or2, stimulus):
        ##Hit
        if (stimulus == True and key1or2 == 1):
            self.antwort = 1
        ##Miss
        if (stimulus == False and key1or2 == 1):
            self.antwort = 2
        ##Hit
        if (stimulus == True and key1or2 == 2):
            self.antwort = 3
        ##Miss
        if (stimulus == False and key1or2 == 2):
            self.antwort = 4

        return self.antwort
    #L efaluate 4 IFC Task
    def getAnswer4IFC (self ,keyAnswer, signalWithStim):
        if (signalWithStim == keyAnswer):
            self.antwort = 1
        else :
            self.antwort = 2
        
        return self.antwort

##
