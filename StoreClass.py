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
from psychopy import core, event, visual
import os
import sys

class VarStore:

    #L initialize the VarStore Object (just one time needed)
    def init(self):
        #L create an StateCheckIn object (Gui)
        self.gui = StateCheckIn()
        self.gui.checkInNameAndType()
        ###name des Objektes###
        
    
        if self.gui.guiInput.OK == False:
            self.gui.core.quit()

    ### Werte von Guiklasse übernehmen
    #L initialize variables with the parameters of the Gui class
        #need no check
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
        if self.experimentType == "Constant Stimuli":
            self.trialComposition = [1,2,11,2,11,12,5,6]
            
#        if self.gui.guiInput.OK == False:
#            self.gui.core.quit()    
        
        self.gui.setVariables(self.experimentType)
        
    def withinMinMax(self, n, minn, maxn):
        return max(min(maxn, n), minn)
   
    def setVariables(self):
        self.initializeFailed = False
        #1-100
        self.numberOfTrials = self.withinMinMax(self.gui.guiInputVar.data[0],1,100) 
        #1-100
        self.trialRounds = self.withinMinMax(self.gui.guiInputVar.data[1],1,100) 
        #0-50
        self.testTrials = self.withinMinMax(self.gui.guiInputVar.data[2],0,50) 
        #0.0 - 10
        self.timeFixationCross = self.withinMinMax(self.gui.guiInputVar.data[3],0,10) 
        self.timeBlankScreen = self.withinMinMax(self.gui.guiInputVar.data[4],0,10) 
        self.timeStimulus = self.withinMinMax(self.gui.guiInputVar.data[5],0.0001,10) 
        self.timeAnswer = self.withinMinMax(self.gui.guiInputVar.data[6],0.0001,10) 
        self.timeFeedback = self.withinMinMax(self.gui.guiInputVar.data[7],0,10) 
        self.timePause = self.withinMinMax(self.gui.guiInputVar.data[8],0,10) 
        #no check
        self.stimulusSizePixels = self.gui.guiInputVar.data[9]
        #0-15
        self.signalIntensity = self.withinMinMax(self.gui.guiInputVar.data[10],1,15)
        #50-200
        self.meanNoise = self.withinMinMax(self.gui.guiInputVar.data[11],50,200) 
        #0-40
        self.standardDeviationNoise = self.withinMinMax(self.gui.guiInputVar.data[12],0,40) 
#
        self.contrastDown = self.gui.guiInputVar.data[13]
        #steps * trialblock have to be less than signalintensity
        self.contrastSteps = self.withinMinMax(self.gui.guiInputVar.data[14],1,10) 
        if (self.contrastSteps* self.trialRounds > self.signalIntensity and self.contrastDown == True):
            self.initializeFailed = True
        self.randomContrast = self.gui.guiInputVar.data[15]
        
        self.dataPath = self.gui.thisDir + os.sep + u'data/' + self.nameVpn + "_Durchgang" + self.durchgangVpn + ".tsv"
        #L checks if savefile already exist to prevent overwriting
#        if os.path.exists(self.dataPath):
#            sys.exit("Datei " + self.dataPath + " existiert bereits!")
        
#        self.instruction = 'Guten Tag, \n\ndas Experiment beginnt in Kürze. \n\nBitte lesen Sie sich die folgenden Instruktionen gut durch. \n\nFalls Sie Fragen haben sollten, stellen Sie diese bitte vor Start des Experiments dem Versuchsleiter. Falls Sie alles Verstanden haben drücken Sie auf "w" für "weiter". \n \n[Weiter] '
        
        if self.experimentType == "Yes/No Task":
            self.instruction2 = 'Es werden Ihnen nun verschiedene Stimuli präsentiert. \n\nEinige Stimuli bestehen nur aus dem Störrauschen, andere bestehen aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nWenn Sie das Signal während des Experiments entdecken, drücken Sie bitte "y". \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]'
            self.instruction3 ='In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt.\n\nFalls Sie gleich nur das Rauschen wahrnehmen sollten, drücken Sie bitte "n". \n\n[Weiter]'
            self.instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der Stimulus. \n\nNachdem der Stimulus wieder ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie in dem Stimulus das Signal erkennen, drücken Sie bitte "y". \n\nFalls Sie das Signal NICHT entdecken können, drücken Sie "n". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
                         
        
        if self.experimentType == "2IFC":
            self.instruction2 = "Im Experiment werden Ihnen immer zwei Stimuli in kurzer Folge präsentiert. \n\nEiner der beiden Stimuli besteht nur aus dem Störrauschen, der andere besteht immer aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]"
            self.instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben, ob das Signal im ersten oder im zweiten Stimulus angezeigt wurde. Dazu drücken Sie, nachdem Sie beide Stimuli gesehen haben, "1" falls Sie das Signal im ersten vermuten, oder "2" falls Sie denken, es wäre im zweiten.\n\n[Weiter]'
            self.instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt vom zweiten. \n\nNachdem der zweite Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie das Signal in dem ersten Stimulus erkennen, drücken Sie bitte "1". \n\nFalls Sie das Signal in dem zweiten Stimulus erkennen, drücken Sie bitte "2". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
            
        if self.experimentType == "4IFC":
            self.instruction2 = 'Im Experiment werden Ihnen immer vier Stimuli in kurzer Folge präsentiert. \n\nDrei der Stimuli bestehen nur aus dem Störrauschen, einer besteht immer aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]'
            self.instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben in welchem der vier Stimuli das Signal angezeigt wurde. Dazu drücken Sie, nachdem Sie die Stimuli gesehen haben, die entsprechende Zahl auf Ihrer Tastatur, also beispielsweise "3" falls Sie das Signal im dritten Stimulus vermuten. \n\n[Weiter]'
            self.instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt von drei weiteren. \n\nNachdem der vierte und letzte Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nDas Signal ist immer in genau einem der vier Stimuli enthalten, für diesen Stimulus drücken Sie bitte die entsprechende Zahlentaste. \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
            
        if self.experimentType == "Constant Stimuli":
            self.instruction2 = 'Im Experiment werden Ihnen immer zwei Stimuli in kurzer Folge präsentiert. \n\nDie Stimuli bestehen immer aus einem Störrauschen und einem Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein solcher Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes ein Stimulus mit einem stärkeren Signal als Beispiel angezeigt. \n\n[Weiter]'
            self.instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit einem stärkeren Signal angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben ob das Signal im ersten oder im zweiten Stimulus stärker. Dazu drücken Sie, nachdem Sie beide Stimuli gesehen haben, "1" falls Sie das erste Signal stärker empfanden, oder "2" falls Sie denken, das zweite war stärker. \n\n[Weiter]'
            self.instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt vom zweiten. \n\nNachdem der zweite Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie das Signal in dem ersten Stimulus für stärker halten, drücken Sie bitte "1". \n\nFalls Sie das Signal in dem zweiten Stimulus für stärker halten, drücken Sie bitte "2". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
























