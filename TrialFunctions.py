# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:38 2018

@author: Leon
"""




class TrialFunctions:
    #L evaluate yes/no task
    def getAnswerYesNo(self, key_yes, stimulus):
            
        '''
        where "key_yes" and "stimulus" have to be a boolean
        
        this function evaluate the given answer of the tested person
        
        it returns a number from 1-4 
        
        1 = Hit, 2 = False alarm, 3 = Correct rejection, 4 = Miss
        '''
        #L Hit --> if "stimulus" was there (True) and answer was yes ("key_yes" == True)
        if (stimulus == True and key_yes == True):
            self.answer = 1
        #L False Alarm  --> if "stimulus" was not there (False) and answer was yes ("key_yes" == True)
        if (stimulus == False and key_yes == True):
            self.answer = 2
        #L Correct Rejection  --> if "stimulus" was not there (False) and answer was no ("key_yes" == False)
        if (stimulus == False and key_yes == False):
            self.answer = 3
        #L Miss --> if "stimulus" was there (True) and answer was no ("key_yes" == False)
        if (stimulus == True and key_yes == False):
            self.answer = 4

        return self.answer
    
    
    #L evaluate 2 IFC task
    def getAnswer2IFC (self, stimulus):
        '''
        where "stimulus" has to be a boolean
        
        this function checks whether the choosed picture contained a stimulus or not
        
        it returns a number 1 if the answer was correct, 2 if the answer was wrong 
        '''
        #L if there was a stimulus --> 1 (correct)
        if stimulus == True:
            self.answer = 1
        #L else in the choosed picture was no stimulus --> 2 (wrong)
        else:
            self.answer = 2
            
        return self.answer
    
    
    #L efaluate 4 IFC Task
    def getAnswer4IFC (self ,key_answer, signal_with_stim):
        '''
        where "key_answer" and "signal" have to be a intiger
        
        this function checks whether the choosed "key_answer" and "signal_with_stim" are the same
        
        it returns 1 if the answer was correct, 2 if the answer was wrong 
        '''
        #if the tested person choosed the picture in wich the stimulus was --> 1
        if (signal_with_stim == key_answer):
            self.answer = 1   
        #else signal_with_stim != key_answer (person picked the wrong picture) --> 2
        else :
            self.answer = 2
        
        return self.answer
    

    def getAnswerConstantStimuli (self, key_1_or_2, difference, constant_pos):
        '''
        where "key_1_or_2", "difference" and "constant_pos" have to be a intiger
        
        this function evaluate wich stimulus has the higher intensity
        
        and checks whether the person has given the right answer
        
        it returns 1 if the answer was correct, 2 if the answer was wrong 
        '''
        
        #L if the "differernz" is greater than zero --> constant stimulus intensity is greater
        if (difference > 0):
            #L "key_1_or_2" and "constant_pos" could be 1 or 2
            #L if the choosed picture is the constant picture
            if(key_1_or_2 == constant_pos):
                self.answer = 1
            #L else the choosed picture is the inconstant picture
            else:
                self.answer = 2
                
        #L if the "differernz" is less than zero --> inconstant stimulus intensity is greater
        if (difference < 0):
            #L if the choosed picture is the inconstant picture
            if(key_1_or_2 != constant_pos):
                self.answer = 1
            #L else if the choosed picture is the constant picture
            else: 
                self.answer = 2

        return self.answer
##
