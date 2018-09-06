# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:44:36 2018

@author: Leon
"""

from __future__ import unicode_literals, division, print_function

# modules aus PsychoPy importieren
from psychopy import core, event, visual
import random
import numpy as np
import sys
import os
from Variablen1 import Variables
from Matrix1 import RandomMatrix
from TrialFunctions import TrialFunctions
from Gui import StateCheckIn
from StoreClass import VarStore

#from state import State

init = VarStore()
init.__init__()


### Sicherstellen, dass Pfad von selbem Verzeichnis wie dieses Skript startet
#_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
#os.chdir(_thisDir)
#
#
#### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
#eingabe = gui.Dlg(title="Signalentdeckung.py")
#
#eingabe.addField("Versuchsperson:")##0
#eingabe.addField("Durchgang:") ##1
#eingabe.addField("Experimenttyp:", choices = ["Yes/No Task", "2IFC"]) ##2
#
#
#
#eingabe.addText("Einstellungen:")
#eingabe.addField("Trialanzahl:",2) ##3
#eingabe.addField("1 = Fixationskreuz",)  ##4
#eingabe.addField("2 = Maske:",) ##5
#eingabe.addField("3 = Stimuluszeit",) ##6
#eingabe.addField("4 = Antwortperiode:",) ##7
#eingabe.addField("5 = Feedbackzeit",) ##8
#eingabe.addField("6 = Pause:",) ##9
#
#eingabe.addField("Pixel Stimulus:", choices = ["32x32", "64x64","128x128"]) ##10
#
#eingabe.addField("Stärke des Signals:",) ##11
#eingabe.addField("Zufällig:",False) ##12
#
#eingabe.addField("Trialablauf",) ##13
#eingabe.show()

# Abbruch falls Cancel gedrückt wurde
if init.gui.eingabe.OK == False:
    init.gui.core.quit()
    
   
    
###### ab hier wenn ok gedrückt wird #######
    
### Werte von Guiklasse übernehmen   
#nameVpn = gui.eingabe.data[0]
#durchgangVpn = gui.eingabe.data[1]
#state = gui.eingabe.data[2]
#trialanzahlNew = gui.eingabe.data[3]
#fixationskreuzNew = gui.eingabe.data[4]
#maskeNew = gui.eingabe.data[5]
#stimuluszeitNew = gui.eingabe.data[6]
#antwortperiodeNew = gui.eingabe.data[7]
#feedbackzeitNew = gui.eingabe.data[8]
#pauseNew = gui.eingabe.data[9]
#
#pixelStimulusNew = gui.eingabe.data[10]
#print(pixelStimulusNew)
#trailablaufNew = gui.eingabe.data[13]
#trailablaufNew.split()
#print(trailablaufNew)
#data_path = gui._thisDir + os.sep + u'data/' + nameVpn + "_Durchgang" + durchgangVpn + ".tsv"

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


#randomHandler.__init__(gui)

var = Variables() 
#if pixelStimulusNew == "32x32":
#    randomHandler.__init__(randomHandler,"Ababa - Kopie.jpg")
#if pixelStimulusNew == "64x64":  
#    randomHandler.__init__(randomHandler,"Ababa 128.jpg")
#if pixelStimulusNew == "128x128":
#    randomHandler.__init__(randomHandler,"Ababa.jpg")
## Variablen

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

#fixiDone = False
#maskeDone = False
#stimulusDone = False
#stimulus2Done = False
#maske2Done = False
#maske3Done = False 
#maske4Done = False 
#antwortDone = False
#feedbackDone = False
#pauseDone = False


zurueckgesetzt = False

clearBeforePress = True

### Zufällig True oder False, entscheidet später ob Stimulus gezeichnet wird oder nicht
stimOrNot = bool(random.getrandbits(1))
stimOrNot2 = False

## Initialisieren mit Gui
trialAblauf = [1,2,3,4,5,6]
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
if init.state == "Yes/No Task":
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
        
    while trial < init.trialanzahlNew: ##Variables.trials
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
                        init.data_path,
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
                        frameRemains = trialClock.getTime() + init.fixationskreuzNew - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        fixiBlack.setAutoDraw(False)
                        i= i+1
                        reseted = False
                
                ##Maske
                if trialAblauf [i]== 2 and i+1 < len(trialAblauf):
                    
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.maskeNew - fenster.monitorFramePeriod * 0.75
                        reseted = True
                    if trialClock.getTime() > frameRemains:
                        
                        i=i+1
                        reseted = False
                ##Stimulus
                if trialAblauf [i]== 3 and i + 1< len(trialAblauf):
                    
                    rauschBild.setAutoDraw(True)
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.stimuluszeitNew - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        rauschBild.setAutoDraw(False)
                        i= i+1
                        reseted = False
                
                ##Antwortperiode
                if trialAblauf [i]== 4 and i+ 1< len(trialAblauf):
                    
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.antwortperiodeNew - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    ##Rutine to clear all events before
                    if clearBeforePress == True:
                        event.clearEvents()
                        clearBeforePress = False 
                    
                    ##Event No
                    if event.getKeys(keyList=["n"]):
                        antwort = trialFkt.getAnswer(False, stimOrNot)
                        antwortZeit = (init.antwortperiodeNew - fenster.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        reseted = False
                        clearBeforePress = True
                    
                    ##Event Yes
                    if event.getKeys(keyList=["y"]):
                        antwort = trialFkt.getAnswer(True, stimOrNot)
                        antwortZeit = (init.antwortperiodeNew - fenster.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        clearBeforePress = True
                        reseted = False
                    
                    if trialClock.getTime() > init.antwortperiodeNew:
                        antwort = 0
                        antwortZeit = 9999
                        i=i+1
                        reseted = False
                
                ##Feedback 
                if trialAblauf[i]== 5 and i + 1< len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.feedbackzeitNew - fenster.monitorFramePeriod * 0.75
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
                        
                ## pause
                
                if trialAblauf [i]== 6 and i +1 < len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.reset() + init.pauseNew - fenster.monitorFramePeriod * 0.75
                        reseted = True
                        
                    if trialClock.getTime() > frameRemains:
                        i = i+1
                        reseted = False
                    
                if event.getKeys(keyList=["escape"])or event.getKeys(keyList=["q"]):
                    fenster.close()
            
           
                fenster.flip()
           

    
print(data)
D = np.array(data)
correct = np.sum(np.logical_or(D[:,0]==1, D[:,0]==3))
print("%i/%i, %g%%"%(correct,init.trialanzahlNew,correct/init.trialanzahlNew*100))
fenster.close()        
