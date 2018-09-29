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

script_dir = script_dir
rel_path = rel_path
image_path = bildpfad
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
    
    def give_image_factory_var(self, store):
        '''
        where "store" has to be a VarStore-object
        
        this function attach the given VarStore-Object to the RandomMatrix-Object
        
        this function has no output
        '''
        self.variables = store
        
    #L initialize the "static" variables 
    def init(self):
############ initialize
        '''
        this function has no input and output
        
        it initilize the "static" variables (wich doen't change over time)
        '''
        #L script directory for loading the picture below
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        
        #L assign the picked pixesize from the gui to the variable "rel_path"
        if self.variables.stimulusSizePixels == "64x64":
            rel_path = "Ababa - Kopie.jpg"
        if self.variables.stimulusSizePixels == "128x128":  
            rel_path = "Ababa 128.jpg"
        if self.variables.stimulusSizePixels == "256x256":
            rel_path = "Ababa.jpg"
        
        #L create the datapath and load the image in "img"
        #L the image needs a white background (fill_value = 255)!!
        image_path = os.path.join(script_dir, rel_path)
        #L img holds the loadet picture
        img = Image.open(image_path)
        
        #L get the pixelvalues out of the image (img) and save it in "pixels"
        pixels = np.asarray(img)
        
        #L needet to work with the pixelmatrix ("pixels")
        pixels.setflags(write=1)
        
        #L save the pixel width  
        self.pixelwidth = len(pixels)
        
        #L create a matrix as big as pixelwidth x pixelwidth full of fill_value = 255 
        #L depht of the matrix is 3 to convert it later into an image-type
        white_matrix = np.full((self.pixelwidth,self.pixelwidth,3), fill_value = 255, dtype=np.uint8)
        

        
        #L "inverseAMatrix" is calculated by the "white_matrix" - "pixels"
        #L where the A is are now values >= 1, everywhere else (where the background was) 0 
        self.inverseAMatrix = white_matrix - pixels

        #L "indizes" save every index where the (colour-)value is bigger or equal 1  
        #L "indizes" is built up lik [[x-axis],[y-axis]]
        self.indizes = np.where(self.inverseAMatrix[:,:,0] >= 1)
            #print(len(indizes[0]))
            #print(len(indizes[1]))
        #L indizes of the x-axis
        self.indizesX = self.indizes[0]
        #L indizes of the y-axis
        self.indizesY = self.indizes[1]
        

        
    #L if the signal intensity is changed start this function to create a new Matrix with given Intensity
    def signalIntensityRefresh(self):
        '''
        this is an "update" function with no input and output
        
        this function create a new matrix where the pixels wich represent the A
        
        get the value of the current "signalIntensity"  
        '''
        #L initialice the countervariable "i"
        i=0
        
        #L len(self.indizes[0]) --> how much pixels represent the A
        while (i < len(self.indizes[0])):
            #L each pixel wich represent the a, now get a new signalIntensity
            #L "inverseAMatrix" needs to save the "signalIntensity" in all 3 levels (depht)
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],0]= self.variables.signalIntensity
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],1]= self.variables.signalIntensity
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],2]= self.variables.signalIntensity
            
            #L if all 3 levels of a pixel got the new "signalIntensity", increas the counter ("i")
            i= i+1
    
    
    def buildMatrixWithSignal(self):
        '''
        where "inverseAMatrix" is a arraytype with depht 3 ([x,y,depht])
        
        this function creats a picture of a grey noise + a stimulus
        
        this function retun an Image-type
        '''
        #L add Matrix with signal ("inverseAMatrix") to the Matrix with the noise 
        #L (wich is created by the function "buildMatrixWithoutSignal")
        noiseSignalMatrix = (self.buildMatrixWithoutSignal())+ self.inverseAMatrix
    
        #L make an image out of the array
        self.image = Image.fromarray(noiseSignalMatrix)
        return self.image


    def buildMatrixWithRandomSignal(self):
        ### überarbeiten
        '''
        were "inverseAMatrix" is a arraytype with depht 3 ([x,y,depht])
        
        this function creates a picture of a grey noise + a stimulus with a random intensity
        
        this function return an Image-type
        '''
        
        #L pick a random value between minContrast and maxContrast
        randomContrast= random.uniform(1,9)
        
        #L initialize countervariable "i"
        i=0
        
        #L each index wich represents the A, gets a new value ("randomContrast")
        while (i < len(self.indizes[0])):
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],0]=randomContrast
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],1]=randomContrast
            self.inverseAMatrix[self.indizesX[i],self.indizesY[i],2]=randomContrast
            i= i+1
        
        #L add Matrix with signal ("inverseAMatrix") to the Matrix with the noise 
        #L (wich is created by the function "buildMatrixWithoutSignal()")
        noiseSignalMatrix = (self.buildMatrixWithoutSignal())+ self.inverseAMatrix

        #L make an image out of the array
        self.image = Image.fromarray(noiseSignalMatrix)
        return self.image



    def buildMatrixWithoutSignal(self):
        '''
        this function has no input
        
        this function create a random, gausian distributed, grey noise-picture
        
        this function return an Image-type
        '''
        #L initialize a random, gausian distributed matrix
        Matrix = np.random.normal(self.variables.meanNoise, self.variables.standardDeviationNoise,[self.pixelwidth,self.pixelwidth])
        #L creats an empty matrix with "depht" 3
        Matrix3D = np.zeros((self.pixelwidth,self.pixelwidth,3), dtype=np.uint8)
        
        #L put all the values from the "Matrix" in each level of the "Matrix3D"
        #L if each level is the same, you get a grey noise (from white over grey to black)
        Matrix3D[:,:,0] = Matrix[:,:]
        Matrix3D[:,:,1] = Matrix[:,:]
        Matrix3D[:,:,2] = Matrix[:,:]
        
        #L make an image out of "Matrix3D"
        self.image = Image.fromarray(Matrix3D)

        return self.image


#    im = Image.effect_noise((1,1), 50)
#randomHandler = RandomMatrix()
#randomHandler.buildMatrixOhneA()
