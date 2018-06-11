from __future__ import unicode_literals, division, print_function

# modules aus PsychoPy importieren
from psychopy import visual, core, event
import random
import numpy as np
from matrix20180528 import RandomMatrix
from Variablen import Variables

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

# Rot/Grün/Schwarz Fixationskreuz
fixiGreen  = newFixi("lime")
fixiRed   = newFixi("red")
fixiBlack = newFixi("black")

### Zufällig True oder False, entscheidet später ob Stimulus gezeichnet wird oder nicht
stimOrNot = bool(random.getrandbits(1))


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
def newFixi (farbe):
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


### Errechnen der Matrix mit Zufallszahlenfunktion
def newRand(stim):
    if (stim == True):
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



    
### Schleife mit Instruktionen die in jedem Frame ausgeführt werden 
while True:
    
    fenster.flip()
    ## instruktionen key wann?
    v_keyInst.draw()
#    
#    image_Zeichnung.draw()
    
    keyInput = event.getKeys()
    
    if(started == True):
        trialClock= core.Clock()
        while trialClock.getTime() < var.fixationskreuz:
                
            fixiBlack.draw()
            fenster.flip()
            
        while trialClock.getTime() < var.fixationskreuz + var.maske:
            
            fenster.flip()
        
        while trialClock.getTime() < var.fixationskreuz + var.maske + var.stimulusZeit:    
            
            image_Zeichnung.draw()
            fenster.flip()
            
        while trialClock.getTime() < var.fixationskreuz + var.maske*2 + var.stimulusZeit:
            
            fenster.flip()
            
        #Or button pressed
        while trialClock.getTime() < var.fixationskreuz + var.maske*2 + var.stimulusZeit + var.antwortperiode:
            
            if 'y' in keyInput:
#        if (newPicture == 0):
#            newPicture = 1
#            counterV = counterV + 1
#            stringCountV = "CountV:%s"%(counterV)
#            v_instruktionCounter = visual.TextStim(fenster, stringCountV +"          "+ stringCountNV, pos =[260, 280])
#            
                if (stimOrNot == True):
                    correctClock= core.Clock()
                    while correctClock.getTime() < var.feedback:
                #image_Zeichnung.setAutoDraw(False)
                        fixiGreen.draw()
                        fenster.flip()
                else:
                    wrongClock= core.Clock()
                    while wrongClock.getTime() < var.feedback:
                #image_Zeichnung.setAutoDraw(False)
                        fixiRed.draw()
                        fenster.flip()
            
                stimOrNot = bool(random.getrandbits(1))
                image_Zeichnung = newRand(stimOrNot)
#            newPicture = 0

### Benutzer sagt Stimulus ist NICHT vorhanden
            if 'n' in keyInput:
#        if (newPicture == 0):
#            newPicture = 1
#            counterNV = counterNV + 1
#            stringCountNV = "CountNV:%s"%(counterNV)
#            v_instruktionCounter = visual.TextStim(fenster, stringCountV +"          "+ stringCountNV, pos =[260, 280])
            
                if (stimOrNot == False):
                    correctClock= core.Clock()
                    while correctClock.getTime() < var.feedback:
                        fixiGreen.draw()
                        fenster.flip()
                else:
                    wrongClock= core.Clock()
                    while wrongClock.getTime() < var.feedback:
                        fixiRed.draw()
                        fenster.flip()
            
                stimOrNot = bool(random.getrandbits(1))
                image_Zeichnung= newRand(stimOrNot)
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
    
                
### Fenster schließen
    if 'q' in keyInput:
        fenster.close()
    if 'escape' in keyInput:
        fenster.close()

#    if (stimulusShowed = True)
        
        
#### Benutzer sagt Stimulus ist vorhanden
#    if 'y' in keyInput:
##        if (newPicture == 0):
##            newPicture = 1
##            counterV = counterV + 1
##            stringCountV = "CountV:%s"%(counterV)
##            v_instruktionCounter = visual.TextStim(fenster, stringCountV +"          "+ stringCountNV, pos =[260, 280])
##            
#        if (stimOrNot == True):
#            correctClock= core.Clock()
#            while correctClock.getTime() < var.feedback:
#                #image_Zeichnung.setAutoDraw(False)
#                fixiGreen.draw()
#                fenster.flip()
#        else:
#            wrongClock= core.Clock()
#            while wrongClock.getTime() < var.feedback:
#                #image_Zeichnung.setAutoDraw(False)
#                fixiRed.draw()
#                fenster.flip()
#            
#        stimOrNot = bool(random.getrandbits(1))
#        image_Zeichnung = newRand(stimOrNot)
##            newPicture = 0
#
#
#### Benutzer sagt Stimulus ist NICHT vorhanden
#    if 'n' in keyInput:
##        if (newPicture == 0):
##            newPicture = 1
##            counterNV = counterNV + 1
##            stringCountNV = "CountNV:%s"%(counterNV)
##            v_instruktionCounter = visual.TextStim(fenster, stringCountV +"          "+ stringCountNV, pos =[260, 280])
#            
#        if (stimOrNot == False):
#            correctClock= core.Clock()
#            while correctClock.getTime() < var.feedback:
#                fixiGreen.draw()
#                fenster.flip()
#        else:
#            wrongClock= core.Clock()
#            while wrongClock.getTime() < var.feedback:
#                fixiRed.draw()
#                fenster.flip()
#            
#        stimOrNot = bool(random.getrandbits(1))
#        image_Zeichnung= newRand(stimOrNot)
##            newPicture = 0
#        