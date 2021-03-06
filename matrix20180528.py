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
class RandomMatrix:

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "Ababa.jpg"
    bildpfad = os.path.join(script_dir, rel_path)

    notFinished = 0
    bild = Image
    #zwischen 0...255
    aKontrast= 3

    img = Image.open(bildpfad)
    pixels = np.asarray(img)
    whiteMatrix = np.full((256,256,3), fill_value = 255, dtype=np.uint8)
    pixels.setflags(write=1)
    ##
    inverseAMatrix = whiteMatrix - pixels
    indizes = np.where(inverseAMatrix[:,:,0] >= 1)
    #print(len(indizes[0]))
    #print(len(indizes[1]))
    indizesX = indizes[0]
    indizesY = indizes[1]

    i=0


    while (i < len(indizes[0])):
        inverseAMatrix[indizesX[i],indizesY[i],0]=aKontrast
        inverseAMatrix[indizesX[i],indizesY[i],1]=aKontrast
        inverseAMatrix[indizesX[i],indizesY[i],2]=aKontrast
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
        Matrix = np.random.normal(Variables().mittelwert, Variables().standartabweichung,[256,256])
        Matrix3D = np.zeros((256,256,3), dtype=np.uint8)
#
        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]

        self.bild = Image.fromarray(Matrix3D)

        return self.bild

#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
