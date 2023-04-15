"""
Created on Thu Oct 14 21:55:30 2021
@author: Umeshika
"""
#import the libraries
from datetime import datetime 
import cv2
import numpy as np
from skimage import  color
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the image
img11 = cv2.imread('b.jpg')
img = cv2.imread('b.jpg').astype(np.float32)
#convert data to gray color with float32
gray_img = color.rgb2gray(img).astype(np.float32)
gray_img11= color.rgb2gray(img)
#otsu function is defined
def otsu(gray_img):
    #Image width and height
    h = gray_img.shape[0]
    w = gray_img.shape[1]
    threshold_t = 0
    max_g = 0
    #every grayscale layer is pixelated
    for t in range(255):
        #array directly taken using  Numpy 
        #define two weight of classes
        x = gray_img[np.where(gray_img < t)]
        x1 = gray_img[np.where(gray_img>=t)]
        #ω0 and ω1 are the proportions of foreground and background
        w0 = len(x)/(h*w)
        w1 = len(x1)/(h*w)
        #foreground mean μ0 
        u0 = np.mean(x) if len(x)>0 else 0
        #background  mean μ1
        u1 = np.mean(x1) if len(x1)>0 else 0
        '''the variance g is calculated using foreground μ0 
        and the background μ1'''
        g = w0*w1*(u0-u1)**2
        #consider segmentation
        if g > max_g :
            max_g = g
            threshold_t = t
    print ('The variance maximum threshold:',threshold_t)
    # take binary image using global thresholding
    gray_img[gray_img<threshold_t] = 0
    gray_img[gray_img>threshold_t] = 255
    return gray_img
#plot the thresholdig image using Otsu's Method 
otsu_img = otsu(gray_img)
cv2.imshow('original image',img11)
cv2.imshow('otsu method image',gray_img11)
cv2.imshow('otsu method image',otsu_img)
cv2.waitKey(0)# Wait 3000ms = 3s
cv2.destroyAllWindows()
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    