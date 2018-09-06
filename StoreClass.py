# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 18:40:36 2018

@author: Leon
"""
from Gui import StateCheckIn
import os

class VarStore(object):
    
    def __init__(self):
        self.gui = StateCheckIn()
    
    ### Werte von Guiklasse übernehmen   
        self.nameVpn = self.gui.eingabe.data[0]
        self.durchgangVpn = self.gui.eingabe.data[1]
        self.state = self.gui.eingabe.data[2]
        self.trialanzahlNew = self.gui.eingabe.data[3]
        self.fixationskreuzNew = self.gui.eingabe.data[4]
        self.maskeNew = self.gui.eingabe.data[5]
        self.stimuluszeitNew = self.gui.eingabe.data[6]
        self.antwortperiodeNew = self.gui.eingabe.data[7]
        self.feedbackzeitNew = self.gui.eingabe.data[8]
        self.pauseNew = self.gui.eingabe.data[9]
        
        self.pixelStimulusNew = self.gui.eingabe.data[10]
        self.signalstaerkeNew = self.gui.eingabe.data[11]
        self.mittelwertNew = self.gui.eingabe.data[12]
        
        self.standartabweichungNew = self.gui.eingabe.data[13]
#        trailablaufNew.split()
        
        self.data_path = self.gui._thisDir + os.sep + u'data/' + self.nameVpn + "_Durchgang" + self.durchgangVpn + ".tsv"
        