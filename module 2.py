import cv2
import numpy as np

minimumRange = np.array([0,133,77],np.uint8) #for min skin color Range
maximumRange = np.array([235,173,127],np.uint8) #for maximum skin color Range
img = cv2.imread("C:/Users/--------/Face.jpg") #reads the detected image from module 1

# change our image bgr to ycr using cvtcolor() method 

YCRimage = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

# apply min or max range on skin area in our image

skinArea = cv2.inRange(YCRimage,minimumRange,maximumRange)
detectedSkin = cv2.bitwise_and(img, img, mask = skinArea)

cv2.imwrite(r"C:\Users\KIIT\Downloads\SkinColor\detectedImage.png", 
            np.hstack([detectedSkin]))
