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
from PIL import Image
<<<<<<< HEAD
from Variablen import Variables
from StoreClass import VarStore

class RandomMatrix:
=======
#from Variablen import Variables
from StoreClass import VarStore
>>>>>>> pascalsgrabbelkiste

    gu = VarStore()
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    if gu.pixelStimulusNew == "32x32":
        rel_path = "Ababa - Kopie.jpg"
    if gu.pixelStimulusNew == "64x64":  
        rel_path = "Ababa 128.jpg"
    if gu.pixelStimulusNew == "128x128":
        rel_path = "Ababa.jpg"
#    rel_path = "Ababa.jpg"
    bildpfad = os.path.join(script_dir, rel_path)

    gu = VarStore()
    
    scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
    if gu.stimulusSizePixels == "32x32":
        relPath = "Ababa - Kopie.jpg"
    if gu.stimulusSizePixels == "64x64":  
        relPath = "Ababa 128.jpg"
    if gu.stimulusSizePixels == "128x128":
        relPath = "Ababa.jpg"
#    relPath = "Ababa.jpg"
    imagePath = os.path.join(scriptDir, relPath)
    
    minContrast = 3
    maxContrast = 20
    
    notFinished = 0
    image = Image
#    var = Variables()
    img = Image.open(imagePath)
    pixels = np.asarray(img)
    pixelwidth = len(pixels)
    print(pixelwidth)
    whiteMatrix = np.full((pixelwidth,pixelwidth,3), fill_value = 255, dtype=np.uint8)
    pixels.setflags(write=1)
    ##
    inverseAMatrix = whiteMatrix - pixels
    print(inverseAMatrix)
    indizes = np.where(inverseAMatrix[:,:,0] >= 1)
        #print(len(indizes[0]))
        #print(len(indizes[1]))
    indizesX = indizes[0]
    indizesY = indizes[1]
    
    i=0
    
    
    while (i < len(indizes[0])):
<<<<<<< HEAD
        inverseAMatrix[indizesX[i],indizesY[i],0]= gu.signalstaerkeNew
        inverseAMatrix[indizesX[i],indizesY[i],1]= gu.signalstaerkeNew
        inverseAMatrix[indizesX[i],indizesY[i],2]= gu.signalstaerkeNew
=======
        inverseAMatrix[indizesX[i],indizesY[i],0]= gu.signalIntensity
        inverseAMatrix[indizesX[i],indizesY[i],1]= gu.signalIntensity
        inverseAMatrix[indizesX[i],indizesY[i],2]= gu.signalIntensity
>>>>>>> pascalsgrabbelkiste
        i= i+1
        #print(inverseAMatrix)


    def buildMatrixWithSignal(self, inverseAMatrix):

        noiseSignalMatrix = (RandomMatrix().buildMatrixWithoutSignal())+ inverseAMatrix

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



<<<<<<< HEAD
    def buildMatrixOhneA(self):
        Matrix = np.random.normal(self.gu.mittelwertNew, self.gu.standartabweichungNew,[self.pixelwidth,self.pixelwidth])
=======
    def buildMatrixWithoutSignal(self):
        Matrix = np.random.normal(self.gu.meanNoise, self.gu.standardDeviationNoise,[self.pixelwidth,self.pixelwidth])
>>>>>>> pascalsgrabbelkiste
        Matrix3D = np.zeros((self.pixelwidth,self.pixelwidth,3), dtype=np.uint8)
#
        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]

        self.image = Image.fromarray(Matrix3D)

<<<<<<< HEAD
        return self.bild
=======
        return self.image
>>>>>>> pascalsgrabbelkiste
    

#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
