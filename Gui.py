# -*- coding: utf-8 -*-
import os
from psychopy import gui, core
import sys
"""
Created on Thu Sep 06 16:32:11 2018

@author: Leon
"""
"""
###############################################################################
############### Verzeichnis alter und neuer Variablennamen ####################
###############################################################################

guiInput = eingabe
thisDir = _thisDir

"""
class StateCheckIn:

    #L if this class is started, it open up our Gui 
    
    thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(thisDir)


    ### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
    guiInput = gui.Dlg(title="Signalentdeckung.py")

    guiInput.addField("Versuchsperson:")##0
    guiInput.addField("Durchgang:") ##1
    guiInput.addField("Experimenttyp:", choices = ["Yes/No Task", "2IFC", "4IFC"]) ##2

    guiInput.addText("Einstellungen:")

    guiInput.addField("Trialanzahl:",10) ##3
    guiInput.addField("Anzahl der Trialblocks", 10)##4
    guiInput.addField("Dauer Fixationskreuz",0.3)  ##5
    guiInput.addField("Dauer Maske:",0.2) ##6
    guiInput.addField("Dauer Stimuluszeit",0.2) ##7
    guiInput.addField("Dauer Antwortperiode:",2) ##8
    guiInput.addField("Dauer Feedbackzeit",0.2) ##9
    guiInput.addField("Dauer Pause:",1) ##10

    guiInput.addField("Stimulusgröße in Pixeln:", choices = ["32x32", "64x64","128x128"]) ##11
    guiInput.addText("Signaleinstellungen:")

    guiInput.addField("Stärke des Signals:",4) ##12
    guiInput.addField("Mittelwert",128) ##13

    guiInput.addField("Standartabweichung",20) ##14
    
#    guiInput.addField("Trialablauf",) #
    guiInput.addField("Kontrast - X je Trialblock",True)##15
    guiInput.addField("Schrittweite",1)##16
    guiInput.addField("Zufällig:",False)##17
    guiInput.show()



    # Abbruch falls Cancel gedrückt wurde
#    if eingabe.OK == False:
#        core.quit()
