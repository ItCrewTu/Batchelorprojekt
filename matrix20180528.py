# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:26:59 2018

@author: Leon
"""  
import PIL
import numpy as np 
from PIL import Image
class RandomMatrix: 

    notFinished = 0
    bild = Image
    #kleienr schönheitsfehler 
    
#    Matrix = np.random.normal(170,20,[256,256])
#    Matrix3D = np.zeros((256,256,3), dtype=np.uint8)

    
    
    
    
    
#    img = Image.open("C:\Users\Leon\Documents\Batchelorprojekt\\Ababa.jpg")
#
#    
##    pixels = img.getdata()
#    pixels = np.asarray(img)
#    
#    whiteMatrix = np.full((256,256,3), fill_value = 255, dtype=np.uint8)
#    inverseMatrix = whiteMatrix - pixels
#    print(inverseMatrix)
    
    
    
    
    def buildMatrixMitA(self):
        data = np.zeros((256,256,3), dtype=np.uint8)
        notFinished = 0
        i=0
        j=0
        while(notFinished == 0):
            rand= np.random.normal(170,20)
            data[i,j]=[rand,rand,rand]
            i=i+1
            if i==256:
                i=0
                j=j+1
                if j==256:
                    notFinished =1
        img = Image.open("C:\Users\Leon\Documents\Batchelorprojekt\\Ababa.jpg")

    
#        pixels = img.getdata()
        pixels = np.asarray(img)
        
        whiteMatrix = np.full((256,256,3), fill_value = 255, dtype=np.uint8)
        
        inverseMatrix = whiteMatrix - pixels
        
        print(inverseMatrix)    
        
        rauschAMatrix = (RandomMatrix().buildMatrixOhneA())+ inverseMatrix
#        rauschAMatrix = rauschAMatrix/(rauschAMatrix.max()/255,0)
        
        ## nochmal machen î
        print(rauschAMatrix)
        self.bild = Image.fromarray(rauschAMatrix)
        return self.bild
    
    
    def buildMatrixOhneA(self):
        data = np.zeros((256,256,3), dtype=np.uint8)
        notFinished = 0
        i=0
        j=0
        while(notFinished == 0):
            rand= np.random.normal(170,20)
            data[i,j]=[rand,rand,rand]
            i=i+1
            if i==256:
                i=0
                j=j+1
                if j==256:
                    notFinished =1
        print(data)
        self.bild = Image.fromarray(data)
        return self.bild

#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
