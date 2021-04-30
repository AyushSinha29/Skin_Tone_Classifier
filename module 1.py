import cv2
  
img = cv2.imread('C:/Users------XYZ.jpg') #Read the input image
  
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('C:/Users/-----/haarcascade_frontalface_default.xml')
  
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.5, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), 
                  (0, 0, 255), 2)
      
    faces = img[y:y + h, x:x + w]
    
    cv2.imshow("Detected Face",faces)
    cv2.imwrite('Face.jpg', faces)
    
  
cv2.imshow('original image', img)
cv2.waitKey()
