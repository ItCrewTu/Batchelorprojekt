from __future__ import unicode_literals, division, print_function

# modules aus PsychoPy importieren
from psychopy import visual, core, event
import random
import numpy as np
from matrix20180528 import RandomMatrix

v_winObj = visual.Window(
        color=[0.5,0.5,0.5],
        colorspace='rgb255',
        fullscr=True,
        size=[800,600],
        units='pix')

#Handler für Rauschmatrix
randomHandler = RandomMatrix()
#clock für bild und voted für zurück setzen

#entscheidet ob stimulus gezeichnet wird oder nicht
stimOrNot = bool(random.getrandbits(1))

#Variablen Initialisieren
counterNV = 0
counterV =0
stringCountV = "Count V: %s"%(counterV)
stringCountNV = "Count NV: %s"%(counterNV)
#wenn neues Rauschen ausgewertet (1) wenn new Picture wieder frei geben (0)
newPicture = 0
answerNotPressed = 0
nextOne = 0


#Beschriftung hinzufügen
v_instruktion = visual.TextStim(v_winObj, 'Klicke in Kreis', pos =[290, 250])
v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
v_vorhanden = visual.TextStim(v_winObj, 'Vorhanden', pos=[290,115])
v_nichtVorhanden = visual.TextStim(v_winObj, 'Nicht Vorhanden', pos=[290,35])
v_beenden = visual.TextStim(v_winObj, 'Beenden', pos=[290,-115])


# Button Vorhanden erzeugen
v_KreisVhd = visual.Circle(v_winObj, radius=20, pos=[290, 75])
v_KreisVhd.setFillColor(color=[0, 255, 255],colorSpace='rgb255')

# Button Nicht Vorhanden erzeugen
v_KreisNichtVhd = visual.Circle(v_winObj, radius=20, pos=[290, 0])
v_KreisNichtVhd.setFillColor(color=[0, 255, 255], colorSpace='rgb255')

# BUtton Beenden erzeugen#
v_stop = visual.Circle(v_winObj, radius=20, pos=[290,-150])
v_stop.setFillColor(color=[255, 0, 0], colorSpace='rgb255')

# Maus erzeugen
v_mausObj = event.Mouse(win = v_winObj)



#provisorisch Umrandung als Feedback
v_posFeedback = visual.Rect(
        win = v_winObj, 
        units= "pix",
        lineWidth= 1,
        width=256, 
        height=256, 
        lineColor="green",
        fillColor="green",
        pos=[0,0]
        )

v_negFeedback = visual.Rect(
        win = v_winObj, 
        units= "pix",
        lineWidth= 1,
        width=256, 
        height=256, 
        lineColor="red",
        fillColor="red",
        pos=[0,-2]
        )


#Zufallszahlenfunktion
def newRand(stim):
    if (stim == True):
        neueMatrix =randomHandler.buildMatrixMitA(randomHandler.inverseAMatrix)
    else: 
        neueMatrix =randomHandler.buildMatrixOhneA()
    image = visual.ImageStim(
            win=v_winObj, name='Matrixoo',
            image=neueMatrix, mask=None,
            ori=0, pos=(0, 0),
            color=[1,1,1], colorSpace='rgb', opacity=1,
            flipHoriz=False, flipVert=False,
            texRes=256, interpolate=True, depth=0.0)

    return image
#Ausführen der Zufallszahlenfunktion
image_Zeichnung = newRand(stimOrNot)


#print(stimOrNot)

# Zeichnen?
#v_KreisVhd.draw()
#v_KreisNichtVhd.draw()
#dot_stim.draw()



#v_winObj.flip()




# notwendig?
v_targetKreis = visual.Circle(v_winObj, radius=20,  pos=[290, 75])
v_targetKreis2 = visual.Circle(v_winObj, radius=20, pos=[290, 0])
#v_stop = visual.Circle(v_winObj, radius=20, pos=[290,-150])



while not v_mausObj.isPressedIn(v_stop):
    v_winObj.flip()
    v_instruktion.draw()
    v_KreisVhd.draw()
    v_KreisNichtVhd.draw()
    v_nichtVorhanden.draw()
    v_vorhanden.draw()
    v_instruktionCounter.draw()
    v_stop.draw()
    v_beenden.draw()
   # while (answerNotPressed == 1):


  #  print("Vorhanden:" % counterV)
   # print("Nicht Vorhanden:" % counterNV)



    image_Zeichnung.draw()

    if (v_mausObj.isPressedIn(v_KreisVhd)):
        if (newPicture == 0):
            newPicture = 1
            counterV = counterV + 1
            stringCountV = "CountV:%s"%(counterV)
            v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
            
            if (stimOrNot == True):
                correctClock= core.Clock()
                while correctClock.getTime() < 0.5:
                    image_Zeichnung.setAutoDraw(False)
                    v_posFeedback.draw()
                    v_winObj.flip()
            else:
                wrongClock= core.Clock()
                while wrongClock.getTime() < 0.5:
                    image_Zeichnung.setAutoDraw(False)
                    v_negFeedback.draw()
                    v_winObj.flip()
            
            stimOrNot = bool(random.getrandbits(1))
            image_Zeichnung = newRand(stimOrNot)
            newPicture = 0


       # v_instruktionCounter.draw()

    if (v_mausObj.isPressedIn(v_KreisNichtVhd)):
        if (newPicture == 0):
            newPicture = 1
            counterNV = counterNV + 1
            stringCountNV = "CountNV:%s"%(counterNV)
            v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
            
            if (stimOrNot == False):
                correctClock= core.Clock()
                while correctClock.getTime() < 0.5:
                    v_posFeedback.draw()
                    v_winObj.flip()
            else:
                wrongClock= core.Clock()
                while wrongClock.getTime() < 0.5:
                    v_negFeedback.draw()
                    v_winObj.flip()
            
            stimOrNot = bool(random.getrandbits(1))
            image_Zeichnung= newRand(stimOrNot)
            newPicture = 0
            

if (v_mausObj.isPressedIn(v_stop)):
    v_winObj.close()

