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
import matplotlib.pyplot as plt
import ctypes
user32 = ctypes.windll.user32
#L works only with 1 monitor ... not 2 
screensizeX = user32.GetSystemMetrics(0)
screensizeY = user32.GetSystemMetrics(1)

#L creats an object that store the parameters of the gui 
init = VarStore()
#L initialize the VarStore-Object with the parameters of the first page of the Gui
init.init()



#L only if the gui button ok is pressed, the rest of the code will be executed
if init.gui.guiInputVar.OK == False:
    init.gui.core.quit()

###### STOP #######
    
#L if the input of the second gui-page is done,    
#L initialize the variables with the parameters of the second page of the Gui    
init.setVariables()




#L Array for the correct answers per Trialblock
data = []




def drawQuit(win):
    '''
    where "win" has to be a visual.Window-type
    
    this function has no output
    
    this function draws "Beenden" on the screen and closes the viusal.Window "win"
    '''
    win.flip()
    quitInst.draw()
    win.flip()
    core.wait(1)
    win.close()
    #core.quit()


#L creats the window for the Experiment
window = visual.Window(
        color=[0,0,0],
        fullscr=True,
        size=[screensizeX,screensizeY],
        units='pix')

#L to be sure that all keys are empty
event.globalKeys.remove(key='all')
#L if "q" or "escape" is pressed, shut down and draw "Beenden..."
event.globalKeys.add(key='q', func=drawQuit, func_args=[window], name='draw quit and shutdown')
event.globalKeys.add(key='escape', func=drawQuit, func_args=[window], name='draw quit and shutup')

quitInst = visual.TextStim(window,
                            'Beenden...',
                            pos =[0, 0])

#L initializeFailed == True if parameters are choosed wich leed to Problems
#L than close the "window"
if(init.initializeFailed == True):
    window.close()

#L creats an object of the class "RandomMatrix"
#L with this object you can request new "noise" or "noise paired with stimulus" -pictures
randomHandler = RandomMatrix()

#L hand the object "init", with the initialized variables, to the object "randomHandler"
randomHandler.giveRandomHandlerVar(init) 

#L initialize the parameter wich are only needed one time
randomHandler.init()
#L load the given signal intensity for the picture (noise paired with stimulus)
randomHandler.signalIntensityRefresh()



#L for blocking in Trial (4IFC)
#L neuer Name --> macht dass erster durch geht (zufallszahl) dannach kommt nicht mehr durch
easyBlock = True
#L intern variable to count trialblocks
trialRounds = 0
#L intern variable to count the trial
trial = 0

#L newSignalIntensity is a intern variable wich will be in- and decreased while the experiment 
#L --> if "kontrastDown" is activated
#L initilized with the signal intensity from the Gui
newSignalIntensity = init.signalIntensity

#L saves the count of correct answers in one try 
save = []


#L response of the testperson, initialized with 0 because that is not answered
responseTestPerson = 0


#L initialize an object of the TrialFunction class, wich has functions to evaluate the testpersons answer
trialFkt = TrialFunctions()

#L choose the text for the instruction to given task
if init.experimentType == "Yes/No Task":
    instruction2 = 'Es werden Ihnen nun verschiedene Stimuli präsentiert. \n\nEinige Stimuli bestehen nur aus dem Störrauschen, andere bestehen aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nWenn Sie das Signal während des Experiments entdecken, drücken Sie bitte "y". \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]'
    instruction3 ='In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt.\n\nFalls Sie gleich nur das Rauschen wahrnehmen sollten, drücken Sie bitte "n". \n\n[Weiter]'
    instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der Stimulus. \n\nNachdem der Stimulus wieder ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie in dem Stimulus das Signal erkennen, drücken Sie bitte "y". \n\nFalls Sie das Signal NICHT entdecken können, drücken Sie "n". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
                 

if init.experimentType == "2IFC":
    instruction2 = "Im Experiment werden Ihnen immer zwei Stimuli in kurzer Folge präsentiert. \n\nEiner der beiden Stimuli besteht nur aus dem Störrauschen, der andere besteht immer aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]"
    instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben, ob das Signal im ersten oder im zweiten Stimulus angezeigt wurde. Dazu drücken Sie, nachdem Sie beide Stimuli gesehen haben, "1" falls Sie das Signal im ersten vermuten, oder "2" falls Sie denken, es wäre im zweiten.\n\n[Weiter]'
    instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt vom zweiten. \n\nNachdem der zweite Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie das Signal in dem ersten Stimulus erkennen, drücken Sie bitte "1". \n\nFalls Sie das Signal in dem zweiten Stimulus erkennen, drücken Sie bitte "2". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
    
if init.experimentType == "4IFC":
    instruction2 = 'Im Experiment werden Ihnen immer vier Stimuli in kurzer Folge präsentiert. \n\nDrei der Stimuli bestehen nur aus dem Störrauschen, einer besteht immer aus dem Rauschen und dem zu entdeckenden Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes wird Ihnen nur das Störrauschen allein als Beispiel angezeigt. \n \n[Weiter]'
    instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun nur das Störrauschen angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben in welchem der vier Stimuli das Signal angezeigt wurde. Dazu drücken Sie, nachdem Sie die Stimuli gesehen haben, die entsprechende Zahl auf Ihrer Tastatur, also beispielsweise "3" falls Sie das Signal im dritten Stimulus vermuten. \n\n[Weiter]'
    instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt von drei weiteren. \n\nNachdem der vierte und letzte Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nDas Signal ist immer in genau einem der vier Stimuli enthalten, für diesen Stimulus drücken Sie bitte die entsprechende Zahlentaste. \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'
    
if init.experimentType == "Constant Stimuli":
    instruction2 = 'Im Experiment werden Ihnen immer zwei Stimuli in kurzer Folge präsentiert. \n\nDie Stimuli bestehen immer aus einem Störrauschen und einem Signal. \n\nIn der Mitte des Bildschirms wird Ihnen nun ein solcher Stimulus mit Signal als Beispiel gezeigt. \n\nAls nächstes ein Stimulus mit einem stärkeren Signal als Beispiel angezeigt. \n\n[Weiter]'
    instruction3 = 'In der Mitte des Bildschirms wird Ihnen nun ein Stimulus mit einem stärkeren Signal angezeigt. \n\nSie haben im Folgenden die Aufgabe, anzugeben ob das Signal im ersten oder im zweiten Stimulus stärker war. Dazu drücken Sie, nachdem Sie beide Stimuli gesehen haben, "1" falls Sie das erste Signal stärker empfanden, oder "2" falls Sie denken, das zweite war stärker. \n\n[Weiter]'
    instruction4 = 'Gleich startet das Experiment. \n\nZunächst wird Ihnen in der Mitte des Bildschirms ein Fixationskreuz angezeigt. Genau dort erscheint wenig später für kurze Zeit der erste Stimulus, gefolgt vom zweiten. \n\nNachdem der zweite Stimulus ausgeblendet wurde, startet die Antwortperiode. \n\nZur Erinnerung: \n\nFalls Sie das Signal in dem ersten Stimulus für stärker halten, drücken Sie bitte "1". \n\nFalls Sie das Signal in dem zweiten Stimulus für stärker halten, drücken Sie bitte "2". \n\nNach Ihrer Entscheidung erhalten Sie ein kurzes Feedback, ob ihre Wahl korrekt war: Ein grünes Kreuz bei richtiger Antwort und ein rotes bei einer falschen. \n\nDanach erscheint wieder das Fixationskreuz und ein neuer Durchgang startet. \n\nWenn Sie nun auf "w" drücken startet das Experiment. Wir empfehlen, Ihre Finger schon auf die entsprechenden Tasten zu legen. \n\n[Weiter]'


### Instruktionen für Keys // Problem Bildschirmgröße
#keyInst = visual.TextStim(window,
#                            'Y -> Stimulus vorhanden \nN -> Stimulus nicht vorhanden \nQ -> Experiment beenden',
#                            pos =[-400, 300])

#L instruction wich is the same in every task
trialInst1 = visual.TextStim(window,'Guten Tag, \n\ndas Experiment beginnt in Kürze. \n\nBitte lesen Sie sich die folgenden Instruktionen gut durch. \n\nFalls Sie Fragen haben sollten, stellen Sie diese bitte vor Start des Experiments dem Versuchsleiter. Falls Sie alles Verstanden haben drücken Sie auf "w" für "weiter". \n \n[Weiter] ', pos =[0, 100])
#L instruction2 which is choosed above
trialInst2 = visual.TextStim(window, instruction2, pos =[400, 0])
#L instruction3 which is choosed above
trialInst3 = visual.TextStim(window, instruction3, pos =[400,0])
#L instruction4 which is choosed above
trialInst4 = visual.TextStim(window, instruction4, pos =[0, 0])

### Maus erzeugen (momentan ungenutzt)
keyInst = event.Mouse(win = window)

#L creats a text-stimulus with "Testtrial abgeschlossen" at the upper center
testTrialOver = visual.TextStim(window, "Testtrial abgeschlossen", pos =[0, 100])



#L function that creats a fixation cross in diffrent colours (var farbe have to be type string)
def newFixi(farbe):
    '''
    where "farbe" has to be a psychopy colour (type string)
    
    this function returns a fixationcross in given ("farbe") colour
    
    the cross has the size of 5 pixels in each direction 
    '''
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

#L initilize fixation cross in red, green, and black colour
fixiGreen  = newFixi("lime")
fixiRed   = newFixi("red")
fixiBlack = newFixi("black")


#
def newRand(stim):
    '''
    where "stim" has to be a boolean
    
    this function creates an image out of a matrix with help of the "randomHandler"
    
    if "stim" == False --> Image (noise)
    
    if "stim" == True --> Image (stimulus + noise)
    
    if "stim" == True and "init.randomContrast == True --> Image (stimulus with random contrast + noise)
    
    it returns an "image" type visual.ImageStim
    '''
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

#L "stimOrNot" is a random boolen
stimOrNot = bool(random.getrandbits(1))
#L "stimOrNot2" is a the opposite of the random boolen stimOrNot
stimOrNot2 = not stimOrNot

#L creats an image wich has a stimulus + noise or just a stimulus
rauschBild = newRand(stimOrNot)


#L image with noise + stimulus wich is initialized just one time at the start of the experiment
#L it is used for the constant stimuli task
rauschBildKonstant = newRand(True)

#L to save the starting signalIntensity, initialized just one time at the start of the experiment 
#L because init.signalIntensity changes over time (if contrast steps down are activated in the gui)
#constantValue = init.signalIntensity

#L for blocking in trial 
easyBlock = True

#L countervariable for the index of the "trialComposition[i]"
i=0

#L "blocked" indicates wether a component is running (blocked = True) or not (blocked = False)
blocked = False
     

    ### INSTRUCTION ###
            
#L if the trial is the first one --> instruction            
if trial == 0:
    
    #L draw "instruction1" (instruction page 1)
    trialInst1.draw()
    window.flip()
    event.waitKeys(keyList=["w"])      
    #L press "w" to continue code (instruction page 2)
    beispielBild = newRand(True)
    beispielBild.draw()
    trialInst2.draw()
    window.flip()
    event.waitKeys(keyList=["w"])      
    #L press "w" to continue code (instruction page 3)
    if init.experimentType == "Constant Stimuli":
        randomHandler.gu.signalIntensity = constantValue + 5
        randomHandler.signalIntensityRefresh()
        beispielBild = newRand(True)
    else:
        beispielBild = newRand(False)
    beispielBild.draw()
    trialInst3.draw()
    window.flip()
    event.waitKeys(keyList=["w"])      
    #L press "w" to continue code (instruction page 4)
    trialInst4.draw()
    window.flip()
    event.waitKeys(keyList=["w"])      
    #L press "w" to continue code (countdowntimer)
    countdownClock = core.CountdownTimer(3.5)

    #L draw the countdown for 3,5 seconds till the experiment starts
    while countdownClock.getTime() > 0:
        

        countdownInst = visual.TextStim(window,
                        int(round(countdownClock.getTime())),
                        pos =[0, 0])
        countdownInst.draw()
        window.flip()


    
    core.wait(0.5)
    ### INSTRUCTION DONE ###
    
    
    ### INITIALIZE TESTTRIALS IF NEEDED ###
    
#L "localTrial" is a variable which has the amount of "init.testTrial"
#L "testTrialCondition" = True
#L if "init.testTrials" != 0
if (init.testTrials != 0):
    localTrial = init.testTrials
    testTrialCondition = True
    
#L if "init.testTrials" == 0 (no test-trials)
#L "localTrial" has the amount of "init.numberOfTrials
#L and "testTrialCondition" = False
else: 
    localTrial = init.numberOfTrials
    testTrialCondition = False
    
    
    ### START OF THE EXPERIMENT ###
  
##L scheme of execution##
    
# while (trialRounds < init.trialRounds): 
#    if trial== localTrial:
#       trialRounds ++ 
#       trial = 0
#    while (trial < localTrial): 
#       if len(init.trialComposition) == i:
#          trial ++
#          i = 0
#       while (len(init.trialComposition) > i) 
#           if trialComposition[i] = x:
#               execute component-x 
#               i++
#          
    

while trialRounds < init.trialRounds:
    
    
    ### BETWEEN TWO TRIALBLOCKS ROUTINE ###
   
    if trial== localTrial:
        #L if maximum trials are reached, 
        #L do the between trialblock-stuff 
        #L trial needs a reset ("trial" = 0)
        trial = 0
        
        
            ### TESTTRIAL CONDITION ###
            
        #L if there are testtrials (only executed one time at the start of the experiment,
        #L if "testTrialCondition" == True)
        if testTrialCondition == True:
            #L set countdownClock on 5s, testTrialInstruction = True and testTrialCondition = False 
            #L from now on "localTrial" has the amount of "init.numberOfTrials"
            localTrial = init.numberOfTrials
            testTrialCondition = False
            countdownClock = core.CountdownTimer(5)
            testTrialInstruction = True
            
            
             ### NO TESTTRIAL CONDITION (SAVE DATA OF TRIALBLOCK) ###
            
        # else (no/no more testtrials)
        else:
            # save the results of the last trialblock
            D = np.array(data)
            # create a new array to save the results of the next trialblock
            data = []
            #0 no answer
            #1 HIT (yesTrue)
            #2 FALSE ALARM (yesFalse)
            #3 CORRECT REJECTION (noTrue)
            #4 MISS (noFalse)
            #correct = HIT + CORRECT REJECTION
            correct = np.sum(np.logical_or(D[:,0]==1, D[:,0]==3))
            print("%i/%i, %g%%"%(correct,init.numberOfTrials,correct/init.numberOfTrials*100))
            #save the amount of correct answers in the array save 
            save.insert(trialRounds,correct)
            #L "trialRounds" ++ to go the next trialround
            trialRounds = trialRounds +1
            countdownClock = core.CountdownTimer(3.5)
            # no more testTrialsInstruction between 2 trialblocks
            testTrialInstruction = False
            
        
            ### CONTRAST DOWN CONDITION ###
            
        #L if "contrastDown" == True, refresh the newSignalIntesity
        if (init.contrastDown == True):
            
            newSignalIntensity= newSignalIntensity - init.contrastSteps
            #L update the "signalIntensity" of the storeunit-object(gu),
            #L wich belongs to the randomHandler-object
            randomHandler.gu.signalIntensity = newSignalIntensity
            #L refresh the signalIntensity of the randomHandler, for the next matrix
            randomHandler.signalIntensityRefresh()
        
        
            ### BETWEEN TRIALBLOCK COUNTER ###
        
        #L counter to show, the Trialblock is over and the next trialblock has
        #L possibly new conditions or settings
        #L "trialRounds" < "init.trialRounds" to be sure its not the last trialblock,
        #L where you show the countdown
        if (trialRounds < init.trialRounds):
            
            #L shows a countdown between 2 trialblocks
            while countdownClock.getTime() > 0:
                
                countdownInst = visual.TextStim(window,
                            int(round(countdownClock.getTime())),
                            pos =[0, 0])
                countdownInst.draw()
                #if the last trialblock was with testtrials, also draw the "testTrialOver"-text
                if(testTrialInstruction == True):
                    testTrialOver.draw()
                window.flip()
        
        
        ### TRIAL ROUTINE ###
        
    #L as long as countervariable "trial" < "localTrial" and "trialRounds" < "init.trialRounds"
    #L so continue the loop
    while trial < localTrial and trialRounds < init.trialRounds: ##Variables.trials

        trialClock= core.Clock()
            
            ### BETWEEN TRIAL RUTINE ###
            
            #L if len(init.trialComposition) == i --> trial is over
        if len(init.trialComposition) == i:
            #L activate a trialClock
            trialClock= core.Clock()
            #L go to next trial
            trial = trial+1
            #L start next trial again at init.trialComposition[0]
            i=0
            #L "easyBlock" is a variable, that is set on True between two trials
            #L to create just one random number per trial (at 4IFC task) 
            easyBlock = True
            
            
                ### SAVE DATA OF TRIAL ###
            
            #L only if it's not a testtrial
            if(testTrialCondition == False):
                data.append([responseTestPerson])
                responseTestPerson = 0
            
                np.savetxt(
                        init.dataPath,
                        data,
                        delimiter="\t"
                        #header="A,B"
                        )
                
                
            ### TRIAL-COMPONENTS ### 
                
        #L one trials is put together out of diffrent trial-components in "init.trialComposition[i]"
        #L #L if len(init.trialComposition) == i --> trial is over
        while (len(init.trialComposition) > i and localTrial > trial):
            
            
            ##FIXATIONCROSS##
            
            #L if trialComposition[i] == 1 than do the fixation cross
            #L this component presents a fixationcross
            if i < len(init.trialComposition) and init.trialComposition [i]== 1 :
                fixiBlack.setAutoDraw(True)
                
                #L @blocked indicates wether a component is running (blocked = True)
                #L or not (blocked = False)
                #L it also guarantee that the "frameRemains" only initialized once at the start of the component
                if not blocked:
                    #L initialize remaining frames (time) stop component
                    #L if remaining time - 3/4 of the monitorFramePeriod is over
                    #L because of the latency of the monitor
                    frameRemains = trialClock.getTime() + init.timeFixationCross - window.monitorFramePeriod * 0.75
                    blocked = True
                    
                #L if time for component is over increase i (next component)
                #L set blocked = False (component is done)
                #L and stop drawing component (setAutodraw(false))
                if trialClock.getTime() > frameRemains:
                    fixiBlack.setAutoDraw(False)
                    i= i+1
                    blocked = False


                ##MASK##
            
            #L if trialComposition[i] == 2 than do the mask
            #L this component shows the background of the window for given time
            if i < len(init.trialComposition) and init.trialComposition [i]== 2 :
                
                #L initilize rutine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeBlankScreen - window.monitorFramePeriod * 0.75
                    blocked = True
                
                
                if trialClock.getTime() > frameRemains:
                    #component is done
                    i=i+1
                    blocked = False
                    
                    
                    ##STIMULUS YES/ NO TASK AND 1. STIMULUS 2IFC##
            
            #L if trialComposition[i] == 3 than do the Stimulus for yes/no task
            #L this component shows picture of (noise) or (noise + stimulus)
            if i < len(init.trialComposition) and init.trialComposition [i]== 3 :
                
                #L initilize rutine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeStimulus - window.monitorFramePeriod * 0.75
                    blocked = True
                    #L @stimOrNot decides wether we have a picture with noise or with noise + stimulus
                    stimOrNot = bool(random.getrandbits(1))
                    rauschBild= newRand(stimOrNot)
                    #L draw that picture
                    rauschBild.setAutoDraw(True) 
                
                
                if trialClock.getTime() > frameRemains:
                    #component is done
                    rauschBild.setAutoDraw(False)
                    i= i+1
                    blocked = False


                ##ANSWERPERIOD YES/NO TASK ##
            
            #L if trialComposition[i] == 4 than do answerperiod of the yes/no task
            #L this component gets an input of "y" yes or "n" no
            #L it evaluate the answer and save it in "responseTestPerson"
            if i < len(init.trialComposition) and init.trialComposition [i]== 4 :

                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeAnswer - window.monitorFramePeriod * 0.75
                    blocked = True
                    #clear the key input list
                    event.clearEvents()

                ##L Event No
                if event.getKeys(keyList=["n"]):
                    #L "trialFkt.getAnswerYesNo() eveluate the answer of the tested person 
                    #L and give back 1-4 (hit, miss, correct rejection, false alarm)
                    #L wich is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswerYesNo(False, stimOrNot)
                    #L antwortZeit zum ermitteln von dauer ... funktioniert noch nicht 
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    #unlock blocked(False) for next component
                    blocked = False
                    
                ##L Event Yes
                if event.getKeys(keyList=["y"]):
                    #L "trialFkt.getAnswerYesNo() eveluate the answer of the tested person 
                    #L and give back 1-5 (hit, miss, correct rejection, false alarm)
                    #L wich is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswerYesNo(True, stimOrNot)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False
                    
                ##L Event no answer
                if trialClock.getTime() > frameRemains:
                    # responseTestPerson = 0 for no answer
                    responseTestPerson = 0
                    antwortZeit = 9999
                    i=i+1
                    blocked = False


                ##FEEDBACK##
            
            #L if trialComposition[i] == 5 than give the feedback
            #L this component is used for assigning the "responseTestPerson" with a green- (for correct),
            #L a red- (for false) or a black-cross
            if i < len(init.trialComposition) and init.trialComposition[i]== 5:
                
                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeFeedback - window.monitorFramePeriod * 0.75
                    blocked = True

#                print(responseTestPerson)
                #L assign responseTestPerson to a cross in the right colour
                
                if responseTestPerson == 0 :
                    #L no answer --> colourFeedback" = black cross
                    colourFeedback = fixiBlack
                    
                if responseTestPerson == 1 or responseTestPerson == 3 :
                    #L hit or correct rejection --> colourFeedback" = green cross
                    colourFeedback = fixiGreen

                if responseTestPerson == 2 or responseTestPerson == 4 :
                    #L miss or false alarm --> "colourFeedback" = red cross
                    colourFeedback = fixiRed
                
                #L draw the cross in evaluated colour
                colourFeedback.setAutoDraw(True)

                #L component is over, set everything back to be ready for the next trialcomponent
                if trialClock.getTime() > frameRemains:
                    colourFeedback.setAutoDraw(False)
                    i= i+1
                    blocked = False

                ## BREAK ##
                
            #L if trialComposition[i] == 6 do a break
            #L this component shows the background of the window for "init.timePause" seconds
            if i < len(init.trialComposition) and init.trialComposition [i]== 6  :
                
                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timePause - window.monitorFramePeriod * 0.75
                    blocked = True

                if trialClock.getTime() > frameRemains:
                    #component is done
                    i = i+1
                    blocked = False
            
            
                ##2. STIMULUS OF 2IFC##
            
            #L if trialComposition[i] == 7 show the second stimulus of the 2IFC -task
            #L this component shows a picture (stimulus + noise) if the first picture was just noise
            #L and shows just noise without stimulus, if the first picture was (stimulus + noise)
            if i < len(init.trialComposition) and init.trialComposition [i]== 7:
                
                #L initilize routine for trial-component
                if not blocked:
                    #L the second stimulus is the negation of the first stimulus
                    stimOrNot2 = not stimOrNot
                    #L create a new matrix with the opposit of the first one 
                    rauschBild= newRand(stimOrNot2)
                    rauschBild.setAutoDraw(True)
                    #calculate the remaining time
                    frameRemains = trialClock.getTime() + init.timeStimulus - window.monitorFramePeriod * 0.75
                    blocked = True
                    
                    
                if trialClock.getTime() > frameRemains:
                    #component is done
                    rauschBild.setAutoDraw(False)
                    i = i+1
                    blocked = False
                    
                    
                ## EVALUATION 2IFC- TASK ##
            
            #L if trialComposition[i] == 8 start the evaluation component
            #L this component listen to the button and if "1" or "2" is pressed, the input gets evaluated
            if i < len(init.trialComposition) and init.trialComposition [i]== 8:
               
                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeAnswer - window.monitorFramePeriod * 0.75
                    blocked = True
                    event.clearEvents()

                ##Event 1
                if event.getKeys(keyList=["1"]):
                    #L if "1" is pressed than "trialFkt.getAnswer2IFC() eveluate the answer of the 
                    #L tested person and give back 1 or 2 (1 for correct and 2 for wrong)
                    #L which is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswer2IFC(stimOrNot)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False

                ##Event 2
                if event.getKeys(keyList=["2"]):
                    #L if "2" is pressed than "trialFkt.getAnswer2IFC() eveluate the answer of the 
                    #L tested person and give back 1 or 2 (1 for correct and 2 for wrong)
                    #L which is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswer2IFC(stimOrNot2)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False
                
                #L if answering time is over, assign 0 to "responseTestPerson"
                if trialClock.getTime() > frameRemains:
                    responseTestPerson = 0
                    antwortZeit = 9999
                    i=i+1
                    blocked = False

                    
                ## STIMULUS 4IFC ##
#               
            #L if trialComposition[i] == 9 show a stimulus of the 4IFC task
            #L this component is executed 4 times each trial, 1 time it shows (stimulus + noise)
            #L and 3 times it shows just noise without the stimulus
            if i < len(init.trialComposition) and init.trialComposition [i]== 9:
                
                #L initilize routine for trial-component
                if not blocked :
                    
                    #L this condition is only true one time in a trial
                    #L @easyBlock is set on True again at "BETWEEN TRIAL ROUTINE"
                    if easyBlock == True : 
                        #L @signalWithStim is a random number between 1 and 4, wich presents the stimulus 
                        signalWithStim = random.randint(1,4)
                        #L @signalNumber = zählvariable 
                        signalNumber=1
                        #L block this codesegment till next trial
                        easyBlock = False
                        
                    #L if the local countervariable "signalNumber" is equal to 
                    #L "signalWithStim, draw a picture with noise + stimulus
                    if signalWithStim == signalNumber :
                        rauschBild= newRand(True)
                        
                    #L if signalWithStim != signalNumber --> draw a picture (just noise)
                    else :
                        rauschBild= newRand(False)
                    
                    #L setAutoDraw(True) for the above initalized "rauschBild"
                    rauschBild.setAutoDraw(True)
                    #L increase the countervariable "signalNumber"
                    signalNumber = signalNumber +1
                    frameRemains = trialClock.getTime() + init.timeStimulus - window.monitorFramePeriod * 0.75
                    blocked = True
                    
                
                if trialClock.getTime() > frameRemains:
                    #component is done
                    rauschBild.setAutoDraw(False)
                    i = i+1
                    blocked = False
                    
                    
                ## EVALUATION 4IFC ##
               
            #L if trialComposition[i] == 10 start the evaluation component
            #L this component listen to the button and evaluate the inputs "1","2","3","4"
            if i < len(init.trialComposition) and init.trialComposition [i]== 10:
                
                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeAnswer - window.monitorFramePeriod * 0.75
                    blocked = True
                    event.clearEvents()

                ##Event 1
                if event.getKeys(keyList=["1"]):
                    #L if "1" is pressed than "trialFkt.getAnswer4IFC() evaluate the answer of the 
                    #L tested person and give back 1 or 2 (1 for correct- and 2 for wrong- answer)
                    #L which is saved in "responseTestPerson"
                    responseTestPerson =  trialFkt.getAnswer4IFC(1,signalWithStim)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False

                ##Event 2
                if event.getKeys(keyList=["2"]):
                    #L evaluate respone with help of "trialFkt.getAnswer4IFC()" and handed parameters
                    responseTestPerson = trialFkt.getAnswer4IFC(2,signalWithStim)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False
                    
                       ##Event 3
                if event.getKeys(keyList=["3"]):
                    #L evaluate respone with help of "trialFkt.getAnswer4IFC()" and handed parameters
                    responseTestPerson = trialFkt.getAnswer4IFC(3,signalWithStim)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False

                ##Event 4
                if event.getKeys(keyList=["4"]):
                    #L evaluate respone with help of "trialFkt.getAnswer4IFC()" and handed parameters
                    responseTestPerson = trialFkt.getAnswer4IFC(4,signalWithStim)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False
                
                #L if answering time is over, assign 0 to "responseTestPerson"
                if trialClock.getTime() > frameRemains:
                    responseTestPerson = 0
                    antwortZeit = 9999
                    i=i+1
                    blocked = False
            
            
                ##CONSTANT STIMULI ##
                
            #L if trialComposition[i] == 11 start the constant stimuli component
            #L this component is executed 2 times each trial 
            #L the first picture shows a constant or an inconsistent stimulus (wich is picked
            #L out of a gausian distribution). A random boolen decide wich one is presented first,
            #L the other one is presented as second
            if i < len(init.trialComposition) and init.trialComposition [i]== 11:
                
                #L initilize routine for trial-component
                if not blocked:
                    
                    #L @easyBlock is only one time every trial True
                    #L so this codesegment below will be executed just 1 time, while this 
                    #L component is executed 2 times 
                    if easyBlock == True:
                        #L @firstOrSecondConstant decide wether constant or 
                        #L inconsistent stimulus is presented first 
                        firstOrSecondConstant = bool(random.getrandbits(1))
                        #L set easyBlock on False till next trial
                        easyBlock = False
                        
                        if (firstOrSecondConstant == True):
                            #@constantPos saves the position of the constant stimulus
                            constantPos = 2
                        else:
                            constantPos = 1
                        
                        #L initialize the inconstantStimuli with is picked out of a
                        #L gausian distribution, with mean "constantValue" and derivation = 1)
                        inconstantStimuli = round(np.random.normal(constantValue, 1),0)
                        #L if the constant stimulus have the same intensity like the inconsisten 
                        #L stimuli, a random boolen decide wether the inconstant intensity gets +1 or -1
                        if (constantValue == inconstantStimuli):
                            plusMinus = bool(random.getrandbits(1))
                            if plusMinus == True:
                                inconstantStimuli = inconstantStimuli + 1
                            if plusMinus == False:
                                inconstantStimuli = inconstantStimuli - 1
                        ##easyBlock over##
                    
                    #L if firstOrSecondConstant == True --> draw the inconstant stimuli
                    if firstOrSecondConstant == True:
                        #L update the randomHandler with the intensity of the inconstant stimului 
                        randomHandler.gu.signalIntensity = inconstantStimuli 
                        randomHandler.signalIntensityRefresh()
                        #L create a picture (noise + stimulus) with updated intensity
                        rauschBild= newRand(True)
                        
                    #L if firstOrSecondConstant != True --> draw the constant stimuli
                    else:
                        #L update the signalIntensity constant stimului 
                        randomHandler.gu.signalIntensity = constantValue
                        randomHandler.signalIntensityRefresh()
                        #L create a picture (noise + stimulus) with updated intensity
                        rauschBild= newRand(True)
                    
                    
                    frameRemains = trialClock.getTime() + init.timeStimulus - window.monitorFramePeriod * 0.75    
                    rauschBild.setAutoDraw(True) 
                    #L negate the variable "firstOrSecondConstant" to execute next time
                    #L the other stimulus
                    firstOrSecondConstant = not firstOrSecondConstant
                    #L blocks the codesegment above till component is done
                    blocked = True
                
                #L draw the picture till time is over, than continue with next component
                #L at index trialComposition[i]
                if trialClock.getTime() > frameRemains:
                    rauschBild.setAutoDraw(False)
                    i= i+1
                    blocked = False#
                    
            ##EVALUATION CONSTANT STIMULI##
             
            #L if trialComposition[i] == 12 start the evaluation for constant stimuli
            #L this component evaluates wether the tested person has given a right answer
            #L --> "responseTestPerson" = 1 or a wrong answer --> "responseTestPerson" = 2
            if i < len(init.trialComposition) and init.trialComposition [i]== 12:
                
                #L initilize routine for trial-component
                if not blocked:
                    frameRemains = trialClock.getTime() + init.timeAnswer - window.monitorFramePeriod * 0.75
                    blocked = True
                    #L @differenz is used to decide wether constant or inconstant intensity is bigger
                    #L differenz > 0 if constant stimulus intensity is bigger 
                    #L differenz < 0 if inconstant stimulus intensity is bigger
                    differenz = constantValue - inconstantStimuli
                    event.clearEvents()


                ##Event 1
                if event.getKeys(keyList=["1"]):
                    #L if "1" is pressed than "trialFkt.getAnswerConstantStimuli()" eveluate
                    #L the answer of the tested person and give back 1 or 2 (1 for correct 
                    #L and 2 for wrong), which is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswerConstantStimuli(1, differenz, constantPos)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False

                ##Event 2
                if event.getKeys(keyList=["2"]):
                    #L if "2" is pressed than "trialFkt.getAnswerConstantStimuli()" eveluate
                    #L the answer of the tested person and give back 1 or 2 (1 for correct 
                    #L and 2 for wrong), which is saved in "responseTestPerson"
                    responseTestPerson = trialFkt.getAnswerConstantStimuli(2, differenz, constantPos)
                    antwortZeit = (init.timeAnswer - window.monitorFramePeriod * 0.75) - (frameRemains - trialClock.getTime())
                    i=i+1
                    blocked = False
                
                #L if answering time is over, assign answer 0 to "responseTestPerson"
                if trialClock.getTime() > frameRemains:
                    responseTestPerson = 0
                    antwortZeit = 9999
                    i=i+1
                    blocked = False
            
            ####
            window.flip()

                
#L show the results with a graph in the console 
print(save)
plt.plot(save)
plt.ylim(0,init.numberOfTrials)
# soll nachher von 1 bis trialrounds gehen
plt.xlim(0,init.trialRounds-1)
plt.show()
drawQuit(window)
