from __future__ import unicode_literals, division, print_function

# modules aus PsychoPy importieren
from psychopy import core, event, gui, visual
import random
import numpy as np
import sys
import os
from Variablen1 import Variables
from Matrix1 import RandomMatrix
#from state import State



### Sicherstellen, dass Pfad von selbem Verzeichnis wie dieses Skript startet
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
eingabe = gui.Dlg(title="Signalentdeckung.py")

eingabe.addField("Versuchsperson:")
eingabe.addField("Durchgang:")
eingabe.addField("State:", choices = ["Yes/No Task", "2AFC"])

eingabe.show()

# Abbruch falls Cancel gedrückt wurde
if eingabe.OK == False:
    core.quit()

nameVpn = eingabe.data[0]
durchgangVpn = eingabe.data[1]
state = eingabe.data[2]

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
        color=[0.5,0.5,0.5],
        fullscr=True,
        size=[800,600],
        units='pix')
started = True
### Handler für Rauschmatrix
randomHandler = RandomMatrix()
## Variablen
var = Variables()
#clock für bild und voted für zurück setzen
antwort= False

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
            interpolate=True, 
            depth=0.0)

    return image

### Ausführen der Zufallszahlenfunktion
image_Zeichnung = newRand(stimOrNot)

if stimOrNot == True:
   stimOrNot2 = False
if stimOrNot == False: 
   stimOrNot2 = True
                
image_Zeichnung2= newRand(stimOrNot2)





            ### Schleife mit Instruktionen die in jedem Frame ausgeführt werden 
if state == "Yes/No Task":
    while trial < Variables.trials:
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
                        
                image_Zeichnung.setAutoDraw(True)
        
                    
            if trialClock.getTime() > var.stimulusZeit and maskeDone and not stimulusDone: 
                
                trialClock.reset()
                image_Zeichnung.setAutoDraw(False)
                stimulusDone = True
                
            ## Maske nach Stimulus 
            if var.maske == 0 and stimulusDone and not maske2Done:
                maske2Done = True
            
        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
                
            if trialClock.getTime() > var.maske and stimulusDone and not maske2Done:
                
                trialClock.reset()
                maske2Done = True
                
            ## Antwortzeit 
            
            if var.antwortperiode == 0 and maske2Done and not antwortDone:
                antwortDone = True
                
            if trialClock.getTime() < var.antwortperiode and maske2Done and not antwortDone:
                        
                v_keyInst.setAutoDraw(True)
                
                
                if clearBeforePress == True:
                    event.clearEvents()
                    clearBeforePress = False 
                    
                if event.getKeys(keyList=["y"]):
                    
                    
                    if (stimOrNot == True):
                        antwortDone = True 
                        antwort = 1
                        v_keyInst.setAutoDraw(False) 
                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 2
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                
                 
                if event.getKeys(keyList=["n"]):
                    
                    
                    if (stimOrNot == False):
                        antwortDone = True 
                        antwort = 3
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 4
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                   
                
            if trialClock.getTime() > var.antwortperiode and maske2Done and not antwortDone: 
                
                
                trialClock.reset()
                v_keyInst.setAutoDraw(False)
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
                
            ##Pause 
            if var.maske == 0:
                maskeDone = True
            
        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
                
            if trialClock.getTime() > var.maske and fixiDone and not maskeDone:
                
                trialClock.reset()
                maskeDone = True
                
                
                
            if var.pause == 0 and feedbackDone and not pauseDone:
                pauseDone = True
        
                    
            if trialClock.getTime() > var.pause and feedbackDone and not pauseDone: 
                
                trialClock.reset()
                pauseDone = True
                
            if pauseDone==True and not zurueckgesetzt:
                fixiDone = False
                maskeDone = False
                stimulusDone = False
                maske2Done = False
                antwortDone = False
                feedbackDone = False
                pauseDone = False
                
                trial = trial + 1
                
                zurueckgesetzt = True
                clearBeforePress = True
                
                stimOrNot = bool(random.getrandbits(1))
                image_Zeichnung= newRand(stimOrNot)
                
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
                
            if event.getKeys(keyList=["escape"])or event.getKeys(keyList=["q"]):
                fenster.close()
        
       
            fenster.flip()
            
    
#print(data)

#fenster.close() 
            
    

                
if state == "2AFC":
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
                        
                image_Zeichnung.setAutoDraw(True)
        
                    
            if trialClock.getTime() > var.stimulusZeit and maskeDone and not stimulusDone: 
                
                image_Zeichnung.setAutoDraw(False)
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
                    
                    
                            
                    image_Zeichnung2.setAutoDraw(True)
            
                        
            if trialClock.getTime() > var.stimulusZeit and maske2Done and not stimulus2Done: 
                    
                    trialClock.reset()
                    image_Zeichnung2.setAutoDraw(False)
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
                        
                v_keyInst.setAutoDraw(True)
                
                
                if clearBeforePress == True:
                    event.clearEvents()
                    clearBeforePress = False 
                    
                if event.getKeys(keyList=["a"]):
                    
                    
                    if (stimOrNot == True):
                        antwortDone = True 
                        antwort = 1
                        v_keyInst.setAutoDraw(False) 
                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 2
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                
                 
                if event.getKeys(keyList=["b"]):
                    
                    
                    if (stimOrNot2 == True):
                        antwortDone = True 
                        antwort = 3
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                        
                    else:
                        antwortDone = True
                        antwort = 4
                        v_keyInst.setAutoDraw(False)
                        trialClock.reset()
                   
                
            if trialClock.getTime() > var.antwortperiode and maske3Done and not antwortDone: 
                
                
                trialClock.reset()
                v_keyInst.setAutoDraw(False)
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
                
                
                
                
                
            ##Pause 
            if var.maske == 0:
                maske4Done = True
            
        #    if trialClock.getTime() < var.maske and fixiDone and not maskeDone:
                
            if trialClock.getTime() > var.maske and fixiDone and not maske4Done:
                
                trialClock.reset()
                maske4Done = True
                
                
                
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
                image_Zeichnung= newRand(stimOrNot)
                if stimOrNot == True:
                   stimOrNot2 = False
                if stimOrNot == False: 
                   stimOrNot2 = True
                                
                image_Zeichnung2= newRand(stimOrNot2)
                
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

fenster.close()        
