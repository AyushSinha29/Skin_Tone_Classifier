from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
from PIL import Image
from numpy import asarray

img = cv.imread('C:/Users/---------/XYZ.jpg') #path of original image
image = cv.imread(r'C:\User-------------\detectedImage.png') #path of detected skin from module 2

image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

resized_image = cv.resize(image, (1200, 600))


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv.imread(image_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image


# convert image to numpy array
data = asarray(image)


# create Pillow image
image2 = Image.fromarray(data)


modified_image = cv.resize(image, (600, 400), interpolation = cv.INTER_AREA)
modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)


clf = KMeans(n_clusters = 2)
labels = clf.fit_predict(modified_image)

counts = Counter(labels)

center_colors = clf.cluster_centers_
# We get ordered colors by iterating through the keys
ordered_colors = [center_colors[i] for i in counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
rgb_colors = [ordered_colors[i] for i in counts.keys()]   


c1=hex_colors[0]
c2=hex_colors[1]

d1=c1.lstrip('#')
d2=c2.lstrip('#')

res1 = int(d1, 16)
res2 = int(d2, 16)

if 8421504>res1>0: #to ignore the darker shade of the background
    fc=res2
    print("The detected skin tone is:",res2," with hex color code as",c2)

else:
    fc=res1
    print("The detected skin tone is:",res1,"(bg color) with hex color code as",c1)  


print("The detected skintone is:")
font = cv.FONT_HERSHEY_TRIPLEX

if 16777215>fc>12619362: #fair range
    print("Fair")
 
    cv.putText(img,'Skin Tone: FAIR',(10,50), font, 1,(0,255,0),2)
    cv.imshow("Result",img)
    cv.waitKey(0)


elif 12619362>fc>10300000:    #mild range
    print("Mild")
    
    cv.putText(img,'Skin Tone: MILD',(10,50), font, 0.5,(0,255,0),2)
    cv.imshow("Result",img)
    cv.waitKey(0)

else:
    print("Dark")    
    cv.putText(img,'Skin Tone: DARK',(10,50), font, 0.5,(0,255,0),2)
    cv.imshow("Result",image)
    cv.waitKey(0)
        

  

 
