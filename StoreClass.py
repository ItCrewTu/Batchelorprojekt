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

        
    def __init__(self):
        self.gui = StateCheckIn()
    
        ###name des Objektes###
        
    ### Werte von Guiklasse übernehmen
        self.nameVpn = self.gui.guiInput.data[0]
        self.durchgangVpn = self.gui.guiInput.data[1]
        self.experimentType = self.gui.guiInput.data[2]
        if self.experimentType == "Yes/No Task":
            self.trialComposition = [1,2,3,4,5,6]
        if self.experimentType == "2IFC":   
            self.trialComposition = [1,2,3,2,7,8,5,6]
        if self.experimentType == "4IFC":   
            self.trialComposition = [1,2,9,2,9,2,9,2,9,10,5,6]
        self.numberOfTrials = self.gui.guiInput.data[3]
        self.timeFixationCross = self.gui.guiInput.data[4]
        self.timeBlankScreen = self.gui.guiInput.data[5]
        self.timeStimulus = self.gui.guiInput.data[6]
        self.timeAnswer = self.gui.guiInput.data[7]
        self.timeFeedback = self.gui.guiInput.data[8]
        self.timePause = self.gui.guiInput.data[9]
        
        self.stimulusSizePixels = self.gui.guiInput.data[10]
        self.signalIntensity = self.gui.guiInput.data[11]
        self.meanNoise = self.gui.guiInput.data[12]

        self.standardDeviationNoise = self.gui.guiInput.data[13]
#        trailablaufNew.split()
        self.randomContrast = self.gui.guiInput.data[14]

        self.dataPath = self.gui.thisDir + os.sep + u'data/' + self.nameVpn + "_Durchgang" + self.durchgangVpn + ".tsv"
