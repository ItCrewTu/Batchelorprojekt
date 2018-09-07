# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, print_function
"""
Created on Wed Jul 18 10:44:36 2018

@author: Leon
"""

"""
###############################################################################
############### Verzeichnis alter und neuer Variablennamen ####################
###############################################################################

Liste enthält alle geänderten Namen dieser Klasse in alphabetischer Reihenfolge:
answerDone = antwortDone
buildMatrixWithoutSignal() = buildMatrixOhneA()
buildMatrixWithRandomSignal() = buildMatrixMitRandomA()
buildMatrixWithSignal() = buildMatrixMitA()
colourFeedback = zeichnungFeedback
dataPath = data_path
guiInput = eingabe
image = bild
imageDrawing = image_Zeichnung
imageDrawing2 = image_Zeichnung2
imagePath = bildpfad
keyInst = v_keyInst
mausObj = v_mausObj
newMatrix = neueMatrix
noiseAMatrix = rauschAMatrix
randomContrast = randomKontrast
relPath = rel_path
responseTestPerson = antwort
reset = zurueckgesetzt
scriptDir = script_dir
thisDir = _thisDir
trialInst = v_trialInst
window = fenster

imageOfSignal = bildname
minContrast = minKontrast
maxContrast = maxContrast
randomContrast = zufallsKontrast
signalContrastIntensity =  kontrastDesZeichens
timeForFixationCross = fixationskreuz
timeForBlankScreen = maske
timeForStimulus = stimulusZeit
timeForAnswer = antwortperiode
timeForFeedback = feedback
timeForPause = pause


standardDeviation = standardabweichungNew
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



# modules aus PsychoPy importieren
from psychopy import core, event, visual
import random
import numpy as np
import sys
import os
#from Variablen1 import Variables
from Matrix1 import RandomMatrix
from TrialFunctions import TrialFunctions
from Gui import StateCheckIn
from StoreClass import VarStore

#from state import State

init = VarStore()
init.__init__()


### Sicherstellen, dass Pfad von selbem Verzeichnis wie dieses Skript startet
#thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
#os.chdir(thisDir)
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
if init.gui.guiInput.OK == False:
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
#stimulusSizePixels = gui.eingabe.data[10]
#print(stimulusSizePixels)
#trailablaufNew = gui.eingabe.data[13]
#trailablaufNew.split()
#print(trailablaufNew)
#dataPath = gui.thisDir + os.sep + u'data/' + nameVpn + "_Durchgang" + durchgangVpn + ".tsv"

### Überprüfen ob Save-File schon existiert, um Überschreiben zu verhindern
#data_path_exists = os.path.exists(dataPath)
##deaktiviert zum testen
#if data_path_exists:
#    sys.exit("Datei " + dataPath + " existiert bereits!")
#

### Array erstellen, in das gespeichert wird
data = []


### Fenster in dem tatsächliches Experiment dargestellt wird
window = visual.Window(
        color=[0,0,0],
        fullscr=True,
        size=[1366,768],
        units='pix')
started = True
### Handler für Rauschmatrix

randomHandler = RandomMatrix()


#randomHandler.__init__(gui)

#var = Variables()
#if stimulusSizePixels == "32x32":
#    randomHandler.__init__(randomHandler,"Ababa - Kopie.jpg")
#if stimulusSizePixels == "64x64":
#    randomHandler.__init__(randomHandler,"Ababa 128.jpg")
#if stimulusSizePixels == "128x128":
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
responseTestPerson = 0

#fixiDone = False
#maskeDone = False
#stimulusDone = False
#stimulus2Done = False
#maske2Done = False
#maske3Done = False
#maske4Done = False
#answerDone = False
#feedbackDone = False
#pauseDone = False


reset = False

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
keyInst = visual.TextStim(window,
                            'Y -> Stimulus vorhanden \nN -> Stimulus nicht vorhanden \nQ -> Experiment beenden',
                            pos =[-400, 300])

### Instruktionen zu Beginn eines Trials
trialInst1 = visual.TextStim(window,
                            'Guten Tag, \n\ndas Experiment beginnt in Kürze. \n\nBitte lesen Sie sich die folgenden Instruktionen gut durch. \n\nFalls Sie Fragen haben sollten, stellen Sie diese bitte vor Start des Experiments dem Versuchsleiter. Falls Sie alles Verstanden haben drücken Sie auf "w" für "weiter". \n \n[Weiter] ',
                            pos =[0, 100])
### Instruktionen zu Beginn eines Trials
trialInst2 = visual.TextStim(window,
                            'Es werden Ihnen nun verschiedene Stimuli präsentiert. \n\nEinige Stimuli bestehen nur aus dem Störrauschen, andere bestehen aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nWenn Sie das Signal während des Experiments entdecken, drücken Sie bitte "y". \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter] ',
                            pos =[500, 0])
### Instruktionen zu Beginn eines Trials
trialInst3 = visual.TextStim(window,
                            'In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt.\n\nFalls Sie gleich nur das Rauschen wahrnehmen sollten, drücken Sie bitte "n". \n\n[Weiter]',
                            pos =[500,0])
### Instruktionen zu Beginn eines Trials
trialInst4 = visual.TextStim(window,
                            'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der Stimulus. \n\nNachdem der Stimulus wieder ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie in dem Stimulus das Signal erkennen, drücken Sie bitte "y". \n\nFalls Sie das Signal NICHT entdecken können, drücken Sie "n". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]',
                            pos =[0, 100])

### Maus erzeugen (momentan ungenutzt)
keyInst = event.Mouse(win = window)

## farbe in string
def newFixi(farbe):
### Positives Feedback (Richtige Antwort)
### Negatives Feedback (Falsche Antwort)

    fixationskreuz = visual.Rect(
            win = window,
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
    if (stim == True and init.randomContrast == True):
        newMatrix =randomHandler.buildMatrixWithRandomSignal(randomHandler.inverseAMatrix)
    elif (stim == True):
        newMatrix =randomHandler.buildMatrixWithSignal(randomHandler.inverseAMatrix)
    else:
        newMatrix =randomHandler.buildMatrixWithoutSignal()
    image = visual.ImageStim(
            win=window,
            name='Matrixoo',
            image=newMatrix,
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
if init.experimentType == "Yes/No Task":
    if trial == 0:





        trialInst1.draw()
        window.flip()
        event.waitKeys(keyList=["w"])      #solange kein schließen möglich
       # window.flip()
        beispielBild = newRand(True)
        beispielBild.draw()
        trialInst2.draw()
        window.flip()
        event.waitKeys(keyList=["w"])      #solange kein schließen möglich
        beispielBild = newRand(False)
        beispielBild.draw()
        trialInst3.draw()
        window.flip()
        event.waitKeys(keyList=["w"])      #solange kein schließen möglich
        trialInst4.draw()
        window.flip()
        event.waitKeys(keyList=["w"])      #solange kein schließen möglich
        countdownClock = core.CountdownTimer(5.5)

        while countdownClock.getTime() > 0:
            ### Instruktionen zu Beginn eines Trials

            countdownInst = visual.TextStim(window,
                            int(round(countdownClock.getTime())),
                            pos =[0, 0])
            countdownInst.draw()
            window.flip()



        i=0
        reseted = False


        core.wait(0.5)


    while trial < init.numberOfTrials: ##Variables.trials
        reset = False
        trialClock= core.Clock()
        while reset == False:

#            print(i)



            ##wenn trialAblauf durchgeführt in nächsten Trial i++
            if len(trialAblauf) == i+1:
                trial = trial+1
                reset = True
                i=0
                stimOrNot = bool(random.getrandbits(1))
                rauschBild= newRand(stimOrNot)
                ##Datenspeicherung
                data.append([responseTestPerson])
                responseTestPerson = 0

                np.savetxt(
                        init.dataPath,
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
                        frameRemains = trialClock.getTime() + init.timeFixationCross - window.monitorFramePeriod * 0.75
                        reseted = True

                    if trialClock.getTime() > frameRemains:
                        fixiBlack.setAutoDraw(False)
                        i= i+1
                        reseted = False

                ##Maske
                if trialAblauf [i]== 2 and i+1 < len(trialAblauf):

                    if not reseted:
                        frameRemains = trialClock.getTime() + init.timeBlankScreen - window.monitorFramePeriod * 0.75
                        reseted = True
                    if trialClock.getTime() > frameRemains:

                        i=i+1
                        reseted = False
                ##Stimulus
                if trialAblauf [i]== 3 and i + 1< len(trialAblauf):

                    rauschBild.setAutoDraw(True)
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.timeStimulus - window.monitorFramePeriod * 0.75
                        reseted = True

                    if trialClock.getTime() > frameRemains:
                        rauschBild.setAutoDraw(False)
                        i= i+1
                        reseted = False

                ##Antwortperiode
                if trialAblauf [i]== 4 and i+ 1< len(trialAblauf):

                    if not reseted:
                        frameRemains = trialClock.getTime() + init.timeAnswer - window.monitorFramePeriod * 0.75
                        reseted = True

                    ##Rutine to clear all events before
                    if clearBeforePress == True:
                        event.clearEvents()
                        clearBeforePress = False

                    ##Event No
                    if event.getKeys(keyList=["n"]):
                        responseTestPerson = trialFkt.getAnswer(False, stimOrNot)
                        antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        reseted = False
                        clearBeforePress = True

                    ##Event Yes
                    if event.getKeys(keyList=["y"]):
                        responseTestPerson = trialFkt.getAnswer(True, stimOrNot)
                        antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                        i=i+1
                        clearBeforePress = True
                        reseted = False

                    if trialClock.getTime() > init.timeAnswer:
                        responseTestPerson = 0
                        antwortZeit = 9999
                        i=i+1
                        reseted = False

                ##Feedback
                if trialAblauf[i]== 5 and i + 1< len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.getTime() + init.timeFeedback - window.monitorFramePeriod * 0.75
                        reseted = True

                    print(responseTestPerson)

                    if responseTestPerson == 0 :
                        colourFeedback = fixiBlack

                    if responseTestPerson == 1 or responseTestPerson == 3 :
                        colourFeedback = fixiGreen

                    if responseTestPerson == 2 or responseTestPerson == 4 :
                        colourFeedback = fixiRed

                    colourFeedback.setAutoDraw(True)

                    if trialClock.getTime() > frameRemains:
                        colourFeedback.setAutoDraw(False)
                        i= i+1
                        reseted = False

                ## pause

                if trialAblauf [i]== 6 and i +1 < len(trialAblauf):
                    if not reseted:
                        frameRemains = trialClock.reset() + init.timePause - window.monitorFramePeriod * 0.75
                        reseted = True

                    if trialClock.getTime() > frameRemains:
                        i = i+1
                        reseted = False

                if event.getKeys(keyList=["escape"])or event.getKeys(keyList=["q"]):
                    window.close()


                window.flip()



print(data)
D = np.array(data)
correct = np.sum(np.logical_or(D[:,0]==1, D[:,0]==3))
print("%i/%i, %g%%"%(correct,init.numberOfTrials,correct/init.numberOfTrials*100))
window.close()
