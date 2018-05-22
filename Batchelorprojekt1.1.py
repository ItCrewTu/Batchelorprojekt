
from __future__ import unicode_literals, division, print_function
 
# modules aus PsychoPy importieren
from psychopy import visual, core, event
import random
import numpy as np

 
v_winObj = visual.Window(
        color=[0.5,0.5,0.5],
        colorspace='rgb255',
        fullscr=True,
        size=[800,600], 
        units='pix')


#Variablen Initialisieren
counterNV = 0
counterV =0
stringCountV = "Count V: %s"%(counterV)
stringCountNV = "Count NV: %s"%(counterNV)
#wenn neues Rauschen ausgewertet (1) wenn new Picture wieder frei geben (0)
newPicture = 0
#
answerNotPressed = 0
nextOne = 0


#Beschriftung hinzufügen
v_instruktion = visual.TextStim(v_winObj, 'Klicke in Oval', pos =[290, 250])
v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
v_instruktionNext = visual.TextStim(v_winObj, "Next", pos =[290, 130])
v_vorhanden = visual.TextStim(v_winObj, 'Vorhanden:', pos=[290,40])
v_nichtVorhanden = visual.TextStim(v_winObj, 'Nicht Vorhanden:', pos=[290,-35])

 
# Kreis erzeugen
v_kreisObj = visual.Circle(v_winObj, radius=20, pos=[290, 75])
v_kreisObj.setFillColor(color=[0, 255, 255],colorSpace='rgb255')
v_nextObj = visual.Circle(v_winObj, radius=20,  pos=[290, 130])

# Kreis erzeugen
v_kreisObj2 = visual.Circle(v_winObj, radius=20, pos=[290, 0])
v_kreisObj2.setFillColor(color=[0, 155, 155], colorSpace='rgb255')
# Maus erzeugen
v_mausObj = event.Mouse(win = v_winObj)


#Zufallszahlenfunktion
def newRand():
   
#Anzahl der Punkte
    n_dots = 100000

#Position der Punkte
    dot_xys = []

    for dot in range(n_dots):

        dot_x = random.uniform(-300, 100)
        dot_y = random.uniform(-200, 200)

        dot_xys.append([dot_x, dot_y])
        #dot_xys = np.random.normal(0,1,[256,256])

#Gradient der Punkte
    randomGradient = []

    for dot in range(n_dots):

        randomNumber = random.gauss (127.5, 100)
    
        randomGradient.append([randomNumber,randomNumber,randomNumber])

#Erstellen der Punkte
    dot_stim = visual.ElementArrayStim(
            win=v_winObj,
            units="pix",
            nElements=n_dots,
            elementTex=None,
            elementMask="gauss",
            xys=dot_xys,
            sizes=3,
            colors=randomGradient,
            colorSpace='rgb255'
            )
    return dot_stim
#Ausführen der Zufallszahlenfunktion
dot_Zeichnung = newRand()

 



# Zeichnen?
#v_kreisObj.draw()
#v_kreisObj2.draw()
#dot_stim.draw()



#v_winObj.flip()




# notwendig?
v_targetKreis = visual.Circle(v_winObj, radius=20,  pos=[290, 75])
v_targetKreis2 = visual.Circle(v_winObj, radius=20, pos=[290, 0])
v_stop = visual.Circle(v_winObj, radius=20, pos=[290,-150])



while not v_mausObj.isPressedIn(v_stop):
    v_winObj.flip()
    v_instruktion.draw()
    v_kreisObj.draw()
    v_kreisObj2.draw()
    v_nichtVorhanden.draw()
    v_vorhanden.draw()
    v_instruktionCounter.draw()
    v_stop.draw()
    v_nextObj.draw()
    v_instruktionNext.draw()
   # while (answerNotPressed == 1):
    dot_Zeichnung.draw()
    
  #  print("Vorhanden:" % counterV)
   # print("Nicht Vorhanden:" % counterNV)
    
  
   

    if (v_mausObj.isPressedIn(v_kreisObj)):
        if (newPicture == 0):
            newPicture = 1
            counterV = counterV + 1
            stringCountV = "CountV:%s"%(counterV)
            v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
        
       # v_instruktionCounter.draw()
        
    if (v_mausObj.isPressedIn(v_kreisObj2)):
        if (newPicture == 0):
            newPicture = 1
            counterNV = counterNV + 1
            stringCountNV = "CountNV:%s"%(counterNV)
            v_instruktionCounter = visual.TextStim(v_winObj, stringCountV +"          "+ stringCountNV, pos =[260, 280])
        
        #erstelle neue Zufallsgaus
    if v_mausObj.isPressedIn(v_nextObj):
        dot_Zeichnung = newRand()  
        newPicture = 0
    
if (v_mausObj.isPressedIn(v_stop)):
    v_winObj.close()
   

