# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:38 2018

@author: Leon
"""




class TrialFunctions:
    #L evaluate yes/no task
    def getAnswerYesNo(self, keyYes, stimulus):
            
        '''
        where "keyYes" and "stimulus" have to be a boolean
        
        this function evaluate the given answer of the tested person
        
        it returns a number from 1-4 
        
        1 = Hit, 2 = False alarm, 3 = Correct rejection, 4 = Miss
        '''
        #L Hit --> if "stimulus" was there (True) and answer was yes ("keyYes" == True)
        if (stimulus == True and keyYes == True):
            self.antwort = 1
        #L False Alarm  --> if "stimulus" was not there (False) and answer was yes ("keyYes" == True)
        if (stimulus == False and keyYes == True):
            self.antwort = 2
        #L Correct Rejection  --> if "stimulus" was not there (False) and answer was no ("keyYes" == False)
        if (stimulus == False and keyYes == False):
            self.antwort = 3
        #L Miss --> if "stimulus" was there (True) and answer was no ("keyYes" == False)
        if (stimulus == True and keyYes == False):
            self.antwort = 4

        return self.antwort
    
    
    #L evaluate 2 IFC task
    def getAnswer2IFC (self, stimulus):
        '''
        where "stimulus" has to be a boolean
        
        this function checks whether the choosed picture contained a stimulus or not
        
        it returns a number 1 if the answer was correct, 2 if the answer was wrong 
        '''
        #L if there was a stimulus --> 1 (correct)
        if stimulus == True:
            self.antwort = 1
        #L else in the choosed picture was no stimulus --> 2 (wrong)
        else:
            self.antwort = 2
            
        return self.antwort
    
    
    #L efaluate 4 IFC Task
    def getAnswer4IFC (self ,keyAnswer, signalWithStim):
        '''
        where "keyAnswer" and "signal" have to be a intiger
        
        this function checks whether the choosed "keyAnswer" and "signalWithStim" are the same
        
        it returns 1 if the answer was correct, 2 if the answer was wrong 
        '''
        #if the tested person choosed the picture in wich the stimulus was --> 1
        if (signalWithStim == keyAnswer):
            self.antwort = 1   
        #else signalWithStim != keyAnswer (person picked the wrong picture) --> 2
        else :
            self.antwort = 2
        
        return self.antwort
    

    def getAnswerConstantStimuli (self, key1or2, differenz, constantPos):
        '''
        where "keyAnswer", "differenz" and "constantPos" have to be a intiger
        
        this function evaluate wich stimulus has the higher intensity
        
        and checks whether the person has given the right answer
        
        it returns 1 if the answer was correct, 2 if the answer was wrong 
        '''
        
        #L if the "differernz" is greater than zero --> constant stimulus intensity is greater
        if (differenz > 0):
            #L "key1or2" and "constantPos" could be 1 or 2
            #L if the choosed picture is the constant picture
            if(key1or2 == constantPos):
                self.antwort = 1
            #L else the choosed picture is the inconstant picture
            else:
                self.antwort = 2
                
        #L if the "differernz" is less than zero --> inconstant stimulus intensity is greater
        if (differenz < 0):
            #L if the choosed picture is the inconstant picture
            if(key1or2 != constantPos):
                self.antwort = 1
            #L else if the choosed picture is the constant picture
            else: 
                self.antwort = 2

        return self.antwort
##
