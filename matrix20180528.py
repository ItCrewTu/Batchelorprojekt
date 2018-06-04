# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:03:08 2018

@author: Leon
"""
import PIL
import numpy as np 
from PIL import Image
class RandomMatrix: 

    notFinished = 0
    bild = Image
    #zwischen 0...255
    aKontrast= 3

    img = Image.open("C:\Users\Leon\Documents\Batchelorprojekt\\Ababa.jpg")
    pixels = np.asarray(img)
    whiteMatrix = np.full((256,256,3), fill_value = 255, dtype=np.uint8)
    pixels.setflags(write=1)
    ##
    inverseAMatrix = whiteMatrix - pixels
    indizes = np.where(inverseAMatrix[:,:,0] >= 1)
    print(len(indizes[0]))
    print(len(indizes[1]))
    indizesX = indizes[0]
    indizesY = indizes[1]
    
    i=0
    
    
    while (i < len(indizes[0])):
        inverseAMatrix[indizesX[i],indizesY[i],0]=aKontrast
        inverseAMatrix[indizesX[i],indizesY[i],1]=aKontrast
        inverseAMatrix[indizesX[i],indizesY[i],2]=aKontrast
        i= i+1
    print(inverseAMatrix)
    
    
    def buildMatrixMitA(self, inverseAMatrix):

        rauschAMatrix = (RandomMatrix().buildMatrixOhneA())+ inverseAMatrix
        
#        rauschAMatrix = rauschAMatrix/(rauschAMatrix.max()/255,0)
#        rauschAMatrix.max(255)
        print(inverseAMatrix)
        self.bild = Image.fromarray(rauschAMatrix)
        return self.bild
    
    
    def buildMatrixOhneA(self):
        Matrix = np.random.normal(170,20,[256,256])
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