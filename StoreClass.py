# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 18:40:36 2018

@author: Leon
"""

"""
###############################################################################
############### Verzeichnis alter und neuer Variablennamen ####################
###############################################################################

guiInput = eingabe
dataPath = data_path
thisDir = _thisDir

imageOfSignal = bildname
minContrast = minKontrast
maxContrast = maxKontrast
randomContrast = zufallsKontrast
signalContrastIntensity =  kontrastDesZeichens


standardDeviationNoise = standardabweichungNew
experimentType = state
numberOfTrials = trialanzahlNew
timeFixationCross = fixationskreuzNew
timeBlankScreen = maskeNew
timeStimulus = stimulusZeitNew
timeAnswer = antwortperiodeNew
timeFeedback = feedbackNew
timePause = pauseNew

meanNoise = mittelwertNew
signalIntensity = signalstaerkeNew

stimulusSizePixels = pixelStimulusNew
"""
from Gui import StateCheckIn
import os

class VarStore(object):

    #L initialize the VarStore Object (just one time needed)
    def __init__(self):
        #L create an StateCheckIn object (Gui)
        self.gui = StateCheckIn()
    
        ###name des Objektes###
        
    ### Werte von Guiklasse übernehmen
    #L initialize variables with the parameters of the Gui class
        self.nameVpn = self.gui.guiInput.data[0]
        self.durchgangVpn = self.gui.guiInput.data[1]
        self.experimentType = self.gui.guiInput.data[2]
        #L which task is selected 
        if self.experimentType == "Yes/No Task":
            self.trialComposition = [1,2,3,4,5,6]
        if self.experimentType == "2IFC":   
            self.trialComposition = [1,2,3,2,7,8,5,6]
        if self.experimentType == "4IFC":   
            self.trialComposition = [1,2,9,2,9,2,9,2,9,10,5,6]
        self.numberOfTrials = self.gui.guiInput.data[3]
        self.trialRounds = self.gui.guiInput.data[4]
        self.timeFixationCross = self.gui.guiInput.data[5]
        self.timeBlankScreen = self.gui.guiInput.data[6]
        self.timeStimulus = self.gui.guiInput.data[7]
        self.timeAnswer = self.gui.guiInput.data[8]
        self.timeFeedback = self.gui.guiInput.data[9]
        self.timePause = self.gui.guiInput.data[10]
        
        self.stimulusSizePixels = self.gui.guiInput.data[11]
        self.signalIntensity = self.gui.guiInput.data[12]
        self.meanNoise = self.gui.guiInput.data[13]

        self.standardDeviationNoise = self.gui.guiInput.data[14]
#        trailablaufNew.split()
        self.contrastDown = self.gui.guiInput.data[15]
        self.contrastSteps = self.gui.guiInput.data[16]
        self.randomContrast = self.gui.guiInput.data[17]

        self.dataPath = self.gui.thisDir + os.sep + u'data/' + self.nameVpn + "_Durchgang" + self.durchgangVpn + ".tsv"
