# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:36 2018

@author: Leon
"""

from __future__ import unicode_literals, division, print_function

# modules aus PsychoPy importieren
from psychopy import core, event, gui, visual
import random
import numpy as np
import sys
import os
from Variablen1 import Variables
from Matrix1 import RandomMatrix
from TrialFunctions import TrialFunctions

#from state import State



### Sicherstellen, dass Pfad von selbem Verzeichnis wie dieses Skript startet
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
eingabe = gui.Dlg(title="Signalentdeckung.py")

eingabe.addField("Versuchsperson:")##0
eingabe.addField("Durchgang:") ##1
eingabe.addField("State:", choices = ["Yes/No Task", "2IFC"]) ##2



eingabe.addText("Einstellungen:")
eingabe.addField("Trialanzahl:",2) ##3
eingabe.addField("1 = Fixationskreuz",)  ##4
eingabe.addField("2 = Maske:",) ##5
eingabe.addField("3 = Stimuluszeit",) ##6
eingabe.addField("4 = Antwortperiode:",) ##7
eingabe.addField("5 = Feedbackzeit",) ##8
eingabe.addField("6 = Pause:",) ##9

eingabe.addField("Pixel Stimulus:", choices = ["32x32", "64x64","128x128"]) ##10

eingabe.addField("Stärke des Signals:",) ##11
eingabe.addField("Zufällig:",False) ##12

eingabe.addField("Trialablauf",) ##13
eingabe.show()

# Abbruch falls Cancel gedrückt wurde
if eingabe.OK == False:
    core.quit()
    
    
###### ab hier wenn ok gedrückt wird #######
    
    
nameVpn = eingabe.data[0]
durchgangVpn = eingabe.data[1]
state = eingabe.data[2]
trialanzahlNew = eingabe.data[3]
fixationskreuzNew = eingabe.data[4]
maskeNew = eingabe.data[5]
stimuluszeitNew = eingabe.data[6]
antwortperiodeNew = eingabe.data[7]
feedbackzeitNew = eingabe.data[8]
pauseNew = eingabe.data[9]

pixelStimulusNew = eingabe.data[10]
print(pixelStimulusNew)
trailablaufNew = eingabe.data[13]
trailablaufNew.split()
data_path = _thisDir + os.sep + u'data/' + nameVpn + "_Durchgang" + durchgangVpn + ".tsv"

### Überprüfen ob Save-File schon existiert, um Überschreiben zu verhindern
#data_path_exists = os.path.exists(data_path)
##deaktiviert zum testen
#if data_path_exists:
#    sys.exit("Datei " + data_path + " existiert bereits!")
#    

### Array erstellen, in das gespeichert wird
data = []


### Fenster in dem tatsächliches Experiment dargestellt wird
fenster = visual.Window(
        color=[0,0,0],
        fullscr=True,
        size=[1366,768],
        units='pix')
started = True
### Handler für Rauschmatrix

randomHandler = RandomMatrix()
## Variablen
var = Variables()
#clock für bild und voted für zurück setzen


flipOn = True

trialWork = True

trial = 0
#0 keine Antwort 
#1 HIT (yesTrue)
#2 FALSE ALARM (yesFalse)
#3 CORRECT REJECTION (noTrue)
#4 MISS (noFalse)
antwort = 0
fixiDone = False
maskeDone = False
stimulusDone = False
stimulus2Done = False
maske2Done = False
maske3Done = False 
maske4Done = False 
antwortDone = False
feedbackDone = False
pauseDone = False


zurueckgesetzt = False

clearBeforePress = True

### Zufällig True oder False, entscheidet später ob Stimulus gezeichnet wird oder nicht
stimOrNot = bool(random.getrandbits(1))
stimOrNot2 = False

## Initialisieren mit Gui
trialAblauf = [trailablaufNew]
print(trialAblauf)
trialFkt = TrialFunctions()
### Variablen Initialisieren
# wenn neues Rauschen ausgewertet (1), wenn new Picture wieder frei gegeben (0)
newPicture = 0
answerNotPressed = 0
nextOne = 0
# Counter momentan ungenutzt !!!
counterNV = 0
counterV = 0
stringCountV = "Count V: %s"%(counterV)
stringCountNV = "Count NV: %s"%(counterNV)


### Instruktionen für Keys // Problem Bildschirmgröße
v_keyInst = visual.TextStim(fenster,
                            'Y -> Stimulus vorhanden \nN -> Stimulus nicht vorhanden \nQ -> Experiment beenden',
                            pos =[-400, 300])

### Instruktionen zu Beginn eines Trials
v_trialInst = visual.TextStim(fenster,
                            '     Sie sehen gerade einen Beispielstimulus. \nFalls Sie diesen in den folgenden Rauschbildern \n      erkennen, druecken Sie Y, falls nicht N. \n         Starten Sie das Experiment mit Y.',
                            pos =[0, 300])


### Maus erzeugen (momentan ungenutzt)
v_mausObj = event.Mouse(win = fenster)

## farbe in string
def newFixi(farbe):
### Positives Feedback (Richtige Antwort)
### Negatives Feedback (Falsche Antwort)

    fixationskreuz = visual.Rect(
            win = fenster,   
            vertices=((0, -5), (0, 5), (0,0), (-5,0), (5, 0)),
            lineWidth=10,
            closeShape=False,
            lineColor = farbe 
#        units= "pix",
#        lineWidth= 1,
#        width=256, 
#        height=256, 
#        lineColor="red",
#        fillColor="red",
#        pos=[0,0]
        )
    return fixationskreuz
# Rot/Grün/Schwarz Fixationskreuz
fixiGreen  = newFixi("lime")
fixiRed   = newFixi("red")
fixiBlack = newFixi("black")


### Errechnen der Matrix mit Zufallszahlenfunktion
def newRand(stim):
    if (stim == True and var.zufallsKontrast == True):
        neueMatrix =randomHandler.buildMatrixMitRandomA(randomHandler.inverseAMatrix)
    elif (stim == True):
        neueMatrix =randomHandler.buildMatrixMitA(randomHandler.inverseAMatrix)
    else: 
        neueMatrix =randomHandler.buildMatrixOhneA()
    image = visual.ImageStim(
            win=fenster, 
            name='Matrixoo',
            image=neueMatrix, 
            mask=None,
            ori=0, pos=(0, 0),
            color=[1,1,1], 
            colorSpace='rgb', 
            opacity=1,
            flipHoriz=False, 
            flipVert=False,
            texRes=256, 
            interpolate=False, 
            depth=0.0)

    return image

### Ausführen der Zufallszahlenfunktion
rauschBild = newRand(stimOrNot)

if stimOrNot == True:
   stimOrNot2 = False
if stimOrNot == False: 
   stimOrNot2 = True
                
rauschBild2= newRand(stimOrNot2)





            ### Schleife mit Instruktionen die in jedem Frame ausgeführt werden 
if state == "Yes/No Task":
    if trial == 0:
        beispielBild = newRand(True)
        beispielBild.draw()
        v_trialInst.draw()
        fenster.flip()
        event.waitKeys(keyList=["y","q","escape"]) #solange kein schließen möglich
        i=0
        reseted = False
        fenster.flip()
        core.wait(1)
        
    while trial < trialanzahlNew: ##Variables.trials
        zurueckgesetzt = False
        trialClock= core.Clock()
        while zurueckgesetzt == False:
            
#            print(i)
            
             
            
            ##wenn trialAblauf durchgeführt in nächsten Trial i++
            if len(trialAblauf) == i+1:
                trial = trial+1
                zurueckgesetzt = True
                i=0
                stimOrNot = bool(random.getrandbits(1))
                rauschBild= newRand(stimOrNot)
                ##Datenspeicherung
                data.append([antwort])
                antwort = 0
                
                np.savetxt(
                        data_path,
                        data,
                        delimiter="\t" 
                        #header="A,B"
                        )
            else:
                
                
                ##Fixationskreuz 
                if trialAblauf [i]== 1 and i +1 < len(trialAblauf):
                    fixiBlack.setAutoDraw(True)
                    ##EInmaliges ausführen
                    if not reseted:
                        frameRemains = trialClock.getTime() + var.fixationskreuz - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        fixiBlack.setAutoDraw(False)
                        i= i+1
                        reseted = False
                
                ##Maske
                if trialAblauf [i]== 2 and i+1 < len(trialAblauf):
                    
                    if not reseted:
                        frameRemains = trialClock.getTime() + var.maske - fenster.monitorFramePeriod * 0.75
                        reseted = True
                    if trialClock.getTime() > frameRemains:
                        
                        i=i+1
                        reseted = False
                ##Stimulus
                if trialAblauf [i]== 3 and i + 1< len(trialAblauf):
                    
                    rauschBild.setAutoDraw(True)
                    if not reseted:
                        frameRemains = trialClock.getTime() + var.stimulusZeit - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        rauschBild.setAutoDraw(False)
                        i= i+1
                        reseted = False
                
                ##Antwortperiode
                if trialAblauf [i]== 4 and i+ 1< len(trialAblauf):
                    
                    if not reseted:
                        frameRemains = trialClock.getTime() + var.antwortperiode - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    ##Rutine to clear all events before
                    if clearBeforePress == True:
                        event.clearEvents()
                        clearBeforePress = False 
                    
                    ##Event No
                    if event.getKeys(keyList=["n"]):
                        antwort = trialFkt.getAnswer(False, stimOrNot)
                        antwortZeit = (var.antwortperiode - fenster.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        reseted = False
                        clearBeforePress = True
                    
                    ##Event Yes
                    if event.getKeys(keyList=["y"]):
                        antwort = trialFkt.getAnswer(True, stimOrNot)
                        antwortZeit = (var.antwortperiode - fenster.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        clearBeforePress = True
                        reseted = False
                    
                    if trialClock.getTime() >var.antwortperiode:
                        antwort = 0
                        antwortZeit = 9999
                        i=i+1
                        reseted = False
                
                ##Feedback 
                if trialAblauf[i]== 5 and i + 1< len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.getTime() +var.feedback- fenster.monitorFramePeriod * 0.75
                        reseted = True
                    
                    print(antwort)
                    
                    if antwort == 0 :
                        zeichnungFeedback = fixiBlack
                    
                    if antwort == 1 or antwort == 3 :
                        zeichnungFeedback = fixiGreen
                        
                    if antwort == 2 or antwort == 4 :
                        zeichnungFeedback = fixiRed
                        
                    zeichnungFeedback.setAutoDraw(True)
               
                    if trialClock.getTime() > frameRemains:
                        zeichnungFeedback.setAutoDraw(False)
                        i= i+1 
                        reseted = False
                
                if trialAblauf [i]== 6 and i +1 < len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.reset() + var.feedback- fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        i = i+1
                        reseted = False
                    
                if event.getKeys(keyList=["escape"])or event.getKeys(keyList=["q"]):
                    fenster.close()
            
           
                fenster.flip()
           
    

                
if state == "2IFC":
        ### Instruktionen vor dem ersten Trial
    if trial == 0:
        beispielBild = newRand(True)
        beispielBild.draw()
        v_trialInst.draw()
        fenster.flip()
        event.waitKeys(keyList=["y","q","escape"])      #solange kein schließen möglich
        fenster.flip()
        core.wait(1)

#        
    while trial < var.trials:
        zurueckgesetzt = False
        trialClock= core.Clock()
        
        while zurueckgesetzt == False:
            
    
            
            ## Fixationskreuz wenn nicht aktiviert übersprungen 
    
            if var.fixationskreuz == 0 and not fixiDone:
                fixiDone = True
                
            if trialClock.getTime() < var.fixationskreuz and not fixiDone:
                        
                fixiBlack.setAutoDraw(True)
        
                    
            if trialClock.getTime() > var.fixationskreuz and not fixiDone: 
                
                trialClock.reset()
                fixiBlack.setAutoDraw(False)
                fixiDone = True
            
            
            
            
            ## Maske 
            
            if var.maske == 0 and fixiDone and not maskeDone:
                maskeDone = True
            
        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
                
            if trialClock.getTime() > var.maske and fixiDone and not maskeDone:
                
                trialClock.reset()
                maskeDone = True
                
        
        

            ## Bild Zeigen
            if var.stimulusZeit == 0 and maskeDone and not stimulusDone:
                stimulusDone = True
                
            if trialClock.getTime() < var.stimulusZeit and maskeDone and not stimulusDone:
                        
                rauschBild.setAutoDraw(True)
        
                    
            if trialClock.getTime() > var.stimulusZeit and maskeDone and not stimulusDone: 
                
                rauschBild.setAutoDraw(False)
                stimulusDone = True
                trialClock.reset()

                
                
            
            ## Maske nach Stimulus 
            if var.maske == 0 and stimulusDone and not maske2Done:
                maske2Done = True
    
            if trialClock.getTime() > var.maske and stimulusDone and not maske2Done:
                
                maske2Done = True
                trialClock.reset()
                

                
                
                
            ## Bild Zeigen
            
            
            if var.stimulusZeit == 0 and maske2Done and not stimulus2Done:
                stimulus2Done = True
            
            
                
                
            if trialClock.getTime() < var.stimulusZeit and maske2Done and not stimulus2Done:
                    
                    
                            
                rauschBild2.setAutoDraw(True)
            
                        
            if trialClock.getTime() > var.stimulusZeit and maske2Done and not stimulus2Done: 
                    
                trialClock.reset()
                    
                rauschBild2.setAutoDraw(False)
                stimulus2Done = True
                    
                    
                    
                    
                    
             ## Maske nach Stimulus 
            if var.maske == 0 and stimulus2Done and not maske3Done:
                maske3Done = True
            
        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
                
            if trialClock.getTime() > var.maske and stimulus2Done and not maske3Done:
                
                trialClock.reset()
                maske3Done = True
                
                
                
                
                
            ## Antwortzeit 
            
            if var.antwortperiode == 0 and maske3Done and not antwortDone:
                antwortDone = True
                
            if trialClock.getTime() < var.antwortperiode and maske3Done and not antwortDone:
                        
                
                
                
                if clearBeforePress == True:
                    event.clearEvents()
                    clearBeforePress = False 
                    
                if event.getKeys(keyList=["a"]):
                    
                    
                    if (stimOrNot == True):
                        antwortDone = True 
                        antwort = 1
    
                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 2

                        trialClock.reset()
                
                 
                if event.getKeys(keyList=["b"]):
                    
                    
                    if (stimOrNot2 == True):
                        antwortDone = True 
                        antwort = 3

                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 4

                        trialClock.reset()
                   
                
            if trialClock.getTime() > var.antwortperiode and maske3Done and not antwortDone: 
                
                
                trialClock.reset()
          
                antwortDone = True
                
            
            
            
            
            
            
            ##Feedback 
            
            if trialClock.getTime() < var.feedback and antwortDone and not feedbackDone:
                
                if antwort == 0 :
                    zeichnungFeedback = fixiBlack
                
                if antwort == 1 or antwort == 3 :
                    zeichnungFeedback = fixiGreen
                    
                if antwort == 2 or antwort == 4 :
                    zeichnungFeedback = fixiRed
                    
                zeichnungFeedback.setAutoDraw(True)
                
            if trialClock.getTime() > var.feedback and antwortDone and not feedbackDone:
                
                zeichnungFeedback.setAutoDraw(False)
                trialClock.reset()
                feedbackDone = True
                
                
                
                
                
#            ##Pause 
#            if var.maske == 0:
#                maske4Done = True
#            
#        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
#                
#            if trialClock.getTime() > var.maske and fixiDone and not maske4Done:
#                
#                trialClock.reset()
#                maske4Done = True
                
                
                
            if var.pause == 0 and feedbackDone and not pauseDone:
                pauseDone = True
        
                    
            if trialClock.getTime() > var.pause and feedbackDone and not pauseDone: 
                
                trialClock.reset()
                pauseDone = True
                
            if pauseDone==True and not zurueckgesetzt:
                fixiDone = False
                maskeDone = False
                stimulusDone = False
                stimulus2Done=False
                maske2Done = False
                maske3Done = False 
                maske4Done = False
                antwortDone = False
                feedbackDone = False
                pauseDone = False
                
                trial = trial + 1
                
                zurueckgesetzt = True
                clearBeforePress = True
                
              

                
                stimOrNot = bool(random.getrandbits(1))
                rauschBild= newRand(stimOrNot)
                if stimOrNot == True:
                   stimOrNot2 = False
                if stimOrNot == False: 
                   stimOrNot2 = True
                                
                rauschBild2= newRand(stimOrNot2)
                
                data.append(
                        [
                               antwort                          
                        ]
                )
                antwort = 0
                np.savetxt(
                        data_path,
                        data,
                        delimiter="\t" 
                        #header="A,B"
                        )
                trialClock.reset()
                
            if event.getKeys(keyList=["escape"])or event.getKeys(keyList=["q"]):
                fenster.close()
        
        
            fenster.flip()
            
    
#print(data)
D = np.array(data)
correct = np.sum(np.logical_or(D[:,0]==1, D[:,0]==3))
print("%i/%i, %g%%"%(correct,var.trials,correct/var.trials*100))
fenster.close()        
