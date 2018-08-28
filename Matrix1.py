# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:03:08 2018

@author: Leon
"""

import numpy as np
import os
import random
from PIL import Image
from Variablen1 import Variables
class RandomMatrix:
    
   
    
    var = Variables()
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
   ##  rel_path = var.bildname 
    rel_path = "Ababa - Kopie.jpg"
     #Ababa (256) und Ababa - Kopie (64) und Ababa 128 (128)
    bildpfad = os.path.join(script_dir, rel_path)

    notFinished = 0
    bild = Image
    
    img = Image.open(bildpfad)
    pixels = np.asarray(img)
    whiteMatrix = np.full((var.pix,var.pix,3), fill_value = 255, dtype=np.uint8)
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
        inverseAMatrix[indizesX[i],indizesY[i],0]=var.kontrastDesZeichens
        inverseAMatrix[indizesX[i],indizesY[i],1]=var.kontrastDesZeichens
        inverseAMatrix[indizesX[i],indizesY[i],2]=var.kontrastDesZeichens
        i= i+1
    #print(inverseAMatrix)
    #def __init__(self, pixel): 
      #  if pixel == 0:
      #      rel_path = "Ababa - Kopie.jpg"
      #  if pixel == 1:
      #      rel_path = "Ababa 128"
       # if pixel == 2:
       #     rel_path = "Ababa"
            
     #   return rel_path

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
        Matrix = np.random.normal(Variables().mittelwert, Variables().standartabweichung,[Variables().pix,Variables().pix])
        Matrix3D = np.zeros((Variables().pix,Variables().pix,3),dtype=np.uint8)

        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]
        self.bild = Image.fromarray(Matrix3D)

        return self.bild
    
    
        if pixel == 0:
            rel_path = "Ababa - Kopie.jpg"
        if pixel == 1:
            rel_path = "Ababa 128"
        if pixel == 2:
            rel_path = "Ababa"
            

#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
