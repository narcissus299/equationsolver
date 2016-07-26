import numpy as np
import cv2

class Cv:

    arConstraint = 20
    hContraint = 10
    wContraint = 10

    def sortCountours(self,contours):
        boundingBoxes = [cv2.boundingRect(c) for c in contours]
        (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes),key=lambda b:b[1][0]))
        return contours

    def getContours(self,im):
        imblur = cv2.GaussianBlur(im,(5,5),0)
        ret,thresh = cv2.threshold(imblur,127,255,cv2.THRESH_BINARY_INV)
        contours, heirarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = self.sortCountours(contours)
        return contours

    def getDimensions(self,contour):
        ar = cv2.contourArea(contour)
        [x,y,w,h] = cv2.boundingRect(contour)
        return [x,y,w,h,ar]

    def extractDigit(self,im,x,y,w,h):
        imchar = im[y:y+h,x:x+w]
        imchar = cv2.resize(imchar,(8,8))
        return imchar

    def getDigits(self,filename):
        im = cv2.imread(filename,0)
        imtemp = im.copy()
        feat = []
        contours = self.getContours(im)
        for c in contours:
            [x,y,w,h,ar] = self.getDimensions(c)
            if ar>self.arConstraint and h>self.hContraint:
                imchar = self.extractDigit(imtemp,x,y,w,h)
                feat.append(imchar)
        return feat

    def getLabels(self,imchar):
        cv2.imshow("Input digit", cv2.resize(imchar,(64,64)))
        label = cv2.waitKey(0)
        return int(label)

    def highlightContours(self,filename):
        im = cv2.imread(filename,0)
        imtemp = im.copy()
        contours = self.getContours(im)
        for c in contours:
            [x,y,w,h,ar] = self.getDimensions(c)
            if ar>self.arConstraint and h>self.hContraint:
                cv2.rectangle(imtemp,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('Test data',cv2.resize(imtemp,(1600,900)))
        cv2.waitKey(0)

    def showContours(self,filename):
        im = cv2.imread(filename,0)
        imtemp = im.copy()
        contours = self.getContours(im)
        for c in contours:
            [x,y,w,h,ar] = self.getDimensions(c)
            if ar>self.arConstraint and h>self.hContraint:
                imchar = self.extractDigit(imtemp, x, y, w, h)
                cv2.imshow('Test data',imchar)
                cv2.waitKey(0)