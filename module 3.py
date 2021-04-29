from sklearn.cluster import KMeans
import cv2
from collections import Counter
from PIL import Image
from numpy import asarray

img = cv2.imread('C:/Users/KIIT/Downloads/SkinColor/detectedImage.png') 
#it is the path of the


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



resized_image = cv2.resize(img, (1200, 600))


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image



# convert image to numpy array
data = asarray(img)


# create Pillow image
image2 = Image.fromarray(data)




modified_image = cv2.resize(img, (600, 400), interpolation = cv2.INTER_AREA)
modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)


clf = KMeans(n_clusters = 2)
labels = clf.fit_predict(modified_image)

counts = Counter(labels)

center_colors = clf.cluster_centers_
# We get ordered colors by iterating through the keys
ordered_colors = [center_colors[i] for i in counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
rgb_colors = [ordered_colors[i] for i in counts.keys()]


    
###############################################################################   
    
#converting the hex color code into decimal 

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
    print("The detected skin tone is:",res1," with hex color code as",c1)  




print("The detected skintone is:")
if 16777215>fc>12619362: #fair range
    print("Fair")
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(img,'Fair',(10,100), font, 1,(0,255,0),2)
    cv2.imshow("Result",img)
    cv2.waitKey(0)

    
elif 12619362>fc>10450000:    #mild range
    print("Mild")
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(img,'Mild',(10,100), font, 1,(0,255,0),2)
    cv2.imshow("Result",img)
    cv2.waitKey(0)
    
else:
    print("Dark")    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(img,'Dark',(10,100), font, 1,(0,255,0),2)
    cv2.imshow("Result",img)
    cv2.waitKey(0)
    
