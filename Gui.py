# -*- coding: utf-8 -*-
import os
from psychopy import gui, core
import sys
"""
Created on Thu Sep 06 16:32:11 2018

@author: Leon
"""

class StateCheckIn:
    
    
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)
    
    
    ### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
    eingabe = gui.Dlg(title="Signalentdeckung.py")
    
    eingabe.addField("Versuchsperson:")##0
    eingabe.addField("Durchgang:") ##1
    eingabe.addField("Experimenttyp:", choices = ["Yes/No Task", "2IFC"]) ##2
    
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
#    if eingabe.OK == False:
#        core.quit()
        
    