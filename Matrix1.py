# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:03:08 2018

@author: Leon
"""


"""
###############################################################################
############### Verzeichnis alter und neuer Variablennamen ####################
###############################################################################

Liste enthält alle geänderten Namen dieser Klasse in alphabetischer Reihenfolge:

scriptDir = script_dir
relPath = rel_path
imagePath = bildpfad
image = bild
noiseSignalMatrix = rauschAMatrix
randomContrast = randomKontrast
buildMatrixWithoutSignal() = buildMatrixOhneA()
buildMatrixWithRandomSignal() = buildMatrixMitRandomA()
buildMatrixWithSignal() = buildMatrixMitA()


imageOfSignal = bildname
minContrast = minKontrast
maxContrast = maxKontrast
randomContrast = zufallsKontrast
signalContrastIntensity =  kontrastDesZeichens
timeForFixationCross = fixationskreuz
timeForBlankScreen = maske
timeForStimulus = stimulusZeit 
timeForAnswer = antwortperiode
timeForFeedback = feedback
timeForPause = pause

meanNoise = mittelwertNew
signalIntensity = signalstaerkeNew

stimulusSizePixels = pixelStimulusNew


"""
import PIL
import numpy as np
import os
import random
from psychopy import core
from PIL import Image
from Variablen import Variables
from StoreClass import VarStore

class RandomMatrix:
    
    def giveRandomHandlerVar(self, init):
        self.gu = init
    #L initilize the "static" variables (just one time needed)
    def init(self):
    
        #L creates an instance of VarStore to have acces to the parameters in the class
#        self.gu = VarStore()
    
        print(self.gu.experimentType)    
        scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
        
        #L assign the picked pixesize to the variable relPath
        if self.gu.stimulusSizePixels == "64x64":
            relPath = "Ababa - Kopie.jpg"
        if self.gu.stimulusSizePixels == "128x128":  
            relPath = "Ababa 128.jpg"
        if self.gu.stimulusSizePixels == "256x256":
            relPath = "Ababa.jpg"
    #    relPath = "Ababa.jpg"
        imagePath = os.path.join(scriptDir, relPath)

        
        img = Image.open(imagePath)
        
        pixels = np.asarray(img)
        #L save the pixel width 
        self.pixelwidth = len(pixels)
        print(self.pixelwidth)
        #L creats matrix with as big as pixelwidth x pixelwidth full of 255 
        whiteMatrix = np.full((self.pixelwidth,self.pixelwidth,3), fill_value = 255, dtype=np.uint8)
        pixels.setflags(write=1)
        #L calculate white Matrix - pixel of the Stimulus pixel by pixel
        #L values > 0 where the A is everywhere else 0 
        self.inverseAMatrix = whiteMatrix - pixels
    #    print(inverseAMatrix)
        #L safe every index wich parameter is bigger than 1  
        #L indizes is like [[x-axis],[y-axis]]
        self.indizes = np.where(self.inverseAMatrix[:,:,0] >= 1)
            #print(len(indizes[0]))
            #print(len(indizes[1]))
        #L indizes of the x-axis
        self.indizesX = self.indizes[0]
        #L indizes of the y-axis
        self.indizesY = self.indizes[1]
        
    def signalIntensityConstantStimuli(self):
        self.gu.signalIntensity = np.random.normal(self.gu.meanNoise, self.gu.standardDeviationNoise)
        
    #if the signal intensity is changed start this function to create a new random Matrix with give Intensity
    def signalIntensityRefresh(self):
        i=0
        
        while (i < len(self.indizes[0])):
    
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],0]= self.gu.signalIntensity
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],1]= self.gu.signalIntensity
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],2]= self.gu.signalIntensity
    
            i= i+1
            #print(inverseAMatrix)
    
    
    def buildMatrixWithSignal(self, inverseAMatrix):
    
        noiseSignalMatrix = (self.buildMatrixWithoutSignal())+ inverseAMatrix
    
    #        noiseSignalMatrix = noiseSignalMatrix/(noiseSignalMatrix.max()/255,0)
    #        noiseSignalMatrix.max(255)
            #print(inverseAMatrix)
        self.image = Image.fromarray(noiseSignalMatrix)
        return self.image


    def buildMatrixWithRandomSignal(self, inverseAMatrix):
        randomContrast= random.uniform(self.minContrast,self.maxContrast)
        i=0
        while (i < len(RandomMatrix.indizes[0])):
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],0]=randomContrast
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],1]=randomContrast
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],2]=randomContrast
            i= i+1
        
        noiseSignalMatrix = (RandomMatrix().buildMatrixWithoutSignal())+ inverseAMatrix

#        noiseSignalMatrix = noiseSignalMatrix/(noiseSignalMatrix.max()/255,0)
#        noiseSignalMatrix.max(255)
        #print(inverseAMatrix)
        self.image = Image.fromarray(noiseSignalMatrix)
        return self.image



    def buildMatrixWithoutSignal(self):
        Matrix = np.random.normal(self.gu.meanNoise, self.gu.standardDeviationNoise,[self.pixelwidth,self.pixelwidth])

        Matrix3D = np.zeros((self.pixelwidth,self.pixelwidth,3), dtype=np.uint8)
#
        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]

        self.image = Image.fromarray(Matrix3D)

        return self.image


#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
