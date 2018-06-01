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
    

    img = Image.open("C:\Users\Leon\Documents\Batchelorprojekt\\Ababa.jpg")
    pixels = np.asarray(img)
    whiteMatrix = np.full((256,256,3), fill_value = 255, dtype=np.uint8)
    inverseAMatrix = whiteMatrix - pixels
    
    
    
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