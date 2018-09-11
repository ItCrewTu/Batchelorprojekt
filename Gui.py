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


    thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(thisDir)


    ### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
    guiInput = gui.Dlg(title="Signalentdeckung.py")

    guiInput.addField("Versuchsperson:")##0
    guiInput.addField("Durchgang:") ##1
    guiInput.addField("Experimenttyp:", choices = ["Yes/No Task", "2IFC", "4IFC"]) ##2

    guiInput.addText("Einstellungen:")

    guiInput.addField("Trialanzahl:",10) ##3
    guiInput.addField("1 = Dauer Fixationskreuz",0.3)  ##4
    guiInput.addField("2 = Dauer Maske:",0.2) ##5
    guiInput.addField("3 = Dauer Stimuluszeit",0.2) ##6
    guiInput.addField("4 = Dauer Antwortperiode:",2) ##7
    guiInput.addField("5 = Dauer Feedbackzeit",0.2) ##8
    guiInput.addField("6 = Dauer Pause:",1) ##9

    guiInput.addField("Stimulusgröße in Pixeln:", choices = ["32x32", "64x64","128x128"]) ##10
    guiInput.addText("Signaleinstellungen:")

    guiInput.addField("Stärke des Signals:",4) ##11
    guiInput.addField("Mittelwert",128) ##12

    guiInput.addField("Standartabweichung",20) ##13
    guiInput.addField("Zufällig:",False) ##14
    guiInput.addField("Trialablauf",) ##15
    guiInput.show()



    # Abbruch falls Cancel gedrückt wurde
#    if eingabe.OK == False:
#        core.quit()
