# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 17:22:56 2018

@author: Leon
"""

class Variables:
    
    #0...255 Helligkeitsunterschied zwischen Rauschen und Bild 
    kontrastDesZeichens = 5
    
    #Bild muss im Ordner des Projekts liegen
    bildname = "Ababa.jpg"
    
    ##Rauschmatrix
    #Mittelwert
    mittelwert = 170
    #Standartabweichung
    standartabweichung = 20
    
    #Zeit ab welcher der versuch als ungültig markiert
    
    zufallsKontrast = True
    minKontrast = 1
    maxKontrast = 10
    #Zeit ab wann die Eingabe frei ist 
    
    
    
    #Trials 100

    trials = 5

    #Zeit 
    fixationskreuz = 0
    
    #länge der Maske 
    maske=0
    
    #Zeit des Stimulus
    stimulusZeit= 1
    #Antwortperiode
    antwortperiode= 2
    #Zeit Feedback
    feedback = 0.5
    #Pause
    pause = 0.5
 
    