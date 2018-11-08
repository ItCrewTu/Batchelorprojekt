# -*- coding: utf-8 -*-
import os
from psychopy import core, gui
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
    def checkInNameAndType (self):
        #L ensure that the path starts from the same directery this script is in
        self.thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
        os.chdir(self.thisDir)
        
        
        ### Eingabefenster für Daten der Vpn, automatisch beim Start geöffnet
        self.guiInput = gui.Dlg(title="Signalentdeckung.py")
        print(33)
        self.guiInput.addField("Versuchsperson:")##0
        self.guiInput.addField("Durchgang:") ##1
        self.guiInput.addField("Experimenttyp:", choices = ["Yes/No Task", "2IFC", "4IFC", "Constant Stimuli"]) ##2
        self.guiInput.show()
        
    def setVariables (self, experimentType):
        
        self.guiInputVar = gui.Dlg(title="Signalentdeckung.py")
        self.guiInputVar.addText("Einstellungen:")
    
        self.guiInputVar.addField("Trialanzahl",10) ##3
        self.guiInputVar.addField("Anzahl der Trialblocks", 5)##4"
        self.guiInputVar.addField("Anzahl der Testtrials",5) ##5
        self.guiInputVar.addField("Dauer Fixationskreuz",0.2)  ##5 +1 nach unte     
        self.guiInputVar.addField("Dauer Maske:",0.1) ##6
        self.guiInputVar.addField("Dauer Stimulus",0.2) ##7
        self.guiInputVar.addField("Dauer Antwortperiode",2) ##8
        self.guiInputVar.addField("Dauer Feedback",0.2) ##9
        self.guiInputVar.addField("Dauer Pause",0.1) ##10
        
    #    guiInput.addField("Zufällig:",False)##17
    #    guiInput.show()
    #    if guiInput.data[11] == True:
        
        self.guiInputVar.addField("Stimulusgröße in Pixeln", choices = ["64x64","128x128","256x256"]) ##11
        self.guiInputVar.addText("Signaleinstellungen:")
    
        self.guiInputVar.addField("Stärke des Signals:",11) ##12
        self.guiInputVar.addField("Mittelwert",128) ##13
    
        self.guiInputVar.addField("Standartabweichung",30) ##14
        if(experimentType == "Constant Stimuli"):
            self.guiInputVar.show()
    #    guiInput.addField("Trialablauf",) #
        self.guiInputVar.addField("Kontrast - X je Trialblock",False)##15
        self.guiInputVar.addField("Schrittweite",2)##16 
        self.guiInputVar.addField("Zufällig",False)##17 nicht immer (zufall wählbar)
        if (experimentType != "Constant Stimuli"):
            self.guiInputVar.show()



    # Abbruch falls Cancel gedrückt wurde
#    if eingabe.OK == False:
#        core.quit()
