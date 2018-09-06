# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:03:08 2018

@author: Leon
"""
import PIL
import numpy as np
import os
import random
from PIL import Image
from Variablen import Variables
from StoreClass import VarStore

class RandomMatrix:

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

    notFinished = 0
    bild = Image
    var = Variables()
    img = Image.open(bildpfad)
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
        inverseAMatrix[indizesX[i],indizesY[i],0]=var.kontrastDesZeichens
        inverseAMatrix[indizesX[i],indizesY[i],1]=var.kontrastDesZeichens
        inverseAMatrix[indizesX[i],indizesY[i],2]=var.kontrastDesZeichens
        i= i+1
        #print(inverseAMatrix)


    def buildMatrixMitA(self, inverseAMatrix):

        rauschAMatrix = (RandomMatrix().buildMatrixOhneA())+ inverseAMatrix

#        rauschAMatrix = rauschAMatrix/(rauschAMatrix.max()/255,0)
#        rauschAMatrix.max(255)
        #print(inverseAMatrix)
        self.bild = Image.fromarray(rauschAMatrix)
        return self.bild


    def buildMatrixMitRandomA(self, inverseAMatrix):
        randomKontrast= random.uniform(Variables().minKontrast,Variables().maxKontrast)
        i=0
        while (i < len(RandomMatrix.indizes[0])):
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],0]=randomKontrast
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],1]=randomKontrast
            inverseAMatrix[RandomMatrix.indizesX[i],RandomMatrix.indizesY[i],2]=randomKontrast
            i= i+1
        
        rauschAMatrix = (RandomMatrix().buildMatrixOhneA())+ inverseAMatrix

#        rauschAMatrix = rauschAMatrix/(rauschAMatrix.max()/255,0)
#        rauschAMatrix.max(255)
        #print(inverseAMatrix)
        self.bild = Image.fromarray(rauschAMatrix)
        return self.bild



    def buildMatrixOhneA(self):
        Matrix = np.random.normal(Variables().mittelwert, Variables().standartabweichung,[self.pixelwidth,self.pixelwidth])
        Matrix3D = np.zeros((self.pixelwidth,self.pixelwidth,3), dtype=np.uint8)
#
        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]

        self.bild = Image.fromarray(Matrix3D)

        return self.bild
    

#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
