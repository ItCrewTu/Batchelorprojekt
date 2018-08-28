# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 17:22:56 2018

@author: Leon
"""

class Variables:
    
    #0...255 Helligkeitsunterschied zwischen Rauschen und Bild 
    kontrastDesZeichens = 6
    
    
    #Bild muss im Ordner des Projekts liegen
    bildname = "Ababa - Kopie.jpg"
    #Ababa (256) und Ababa - Kopie (64) und Ababa 128 (128)
    
    ##Rauschmatrix
    #Mittelwert
    mittelwert = 130
    #Standartabweichung
    standartabweichung = 25
    
    #Zeit ab welcher der versuch als ungültig markiert
    
    zufallsKontrast = False
    minKontrast = 1
    maxKontrast = 10
    #Zeit ab wann die Eingabe frei ist 
    
    #Pixel pix x pix 
    pix = 64
    
    #Trials 100

    trials = 5

    #Zeit 
    fixationskreuz = 0.25
    
    #länge der Maske 
    maske=0.3
    
    #Zeit des Stimulus
    stimulusZeit= 2.0/60.0
    #Antwortperiode
    antwortperiode= 2
    #Zeit Feedback
    feedback = 1
    #Pause
    pause = 0.5
 
    